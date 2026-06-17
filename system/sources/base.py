"""Base class para coletores de fontes publicas."""
from datetime import datetime, date
from typing import Iterable
import json
import sys
import os
from pathlib import Path

# Permite import quando rodado de fora
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Fix SSL no Windows: usar o cert store nativo do OS via truststore
# Resolve certificados que nao estao no bundle do certifi/Python
try:
    import truststore
    truststore.inject_into_ssl()
except ImportError:
    pass

import config
import db


class BaseCollector:
    """Classe base para coletores de fontes publicas.

    Subclasses devem definir:
    - source_name: str            (ex: 'cme_cbot', 'bcb', 'cftc_cot')
    - cadence: str                ('daily', 'weekly', 'monthly')
    - description: str            (1 linha sobre a fonte)

    E implementar:
    - fetch() -> Iterable[dict]   retorna registros normalizados

    Schema esperado de cada dict retornado por fetch():
    {
        'data_referencia': '2026-05-20',     # YYYY-MM-DD
        'tipo': 'preco',                      # 'preco' | 'estoque' | 'producao' | etc
        'commodity': 'soja_cbot',             # opcional, identificador
        'metrica': 'fechamento',              # nome da metrica
        'valor': 1234.56,                     # float
        'unidade': 'USD/bushel',              # str
        'contexto': '...',                    # opcional
        'raw': {...}                          # opcional, dado original
    }
    """
    source_name: str = "base"
    cadence: str = "daily"
    description: str = ""
    enabled: bool = True

    def fetch(self) -> Iterable[dict]:
        raise NotImplementedError(
            f"Coletor {self.source_name} ainda nao tem fetch() implementado. "
            f"Veja system/sources/{self.source_name}.py"
        )

    def save_to_db(self, records: list[dict]) -> int:
        if not records:
            return 0
        saved = 0
        with db.connect() as conn:
            for r in records:
                # UPSERT (last-write-wins): o preco do DIA CORRENTE evolui durante o
                # pregao (barra diaria do Yahoo atualiza com delay ~15min). Com o antigo
                # INSERT OR IGNORE, a 1a captura do dia travava e todo run seguinte era
                # ignorado -> preco congelado o dia inteiro. Para serie de mercado, a
                # leitura mais recente e a correta; re-fetch de dia passado so reescreve
                # o mesmo valor (no-op). Chave = UNIQUE(fonte,data_referencia,tipo,metrica,commodity).
                cursor = conn.execute(
                    """
                    INSERT INTO dados_publicos
                    (fonte, data_referencia, tipo, commodity, metrica, valor, unidade, contexto, raw_json)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(fonte, data_referencia, tipo, metrica, commodity)
                    DO UPDATE SET valor=excluded.valor,
                                  unidade=excluded.unidade,
                                  contexto=excluded.contexto,
                                  raw_json=excluded.raw_json
                    """,
                    (
                        self.source_name,
                        r.get("data_referencia"),
                        r.get("tipo", "indef"),
                        r.get("commodity"),
                        r.get("metrica", "valor"),
                        r.get("valor"),
                        r.get("unidade"),
                        r.get("contexto"),
                        json.dumps(r.get("raw"), ensure_ascii=False, default=str) if r.get("raw") else None,
                    ),
                )
                if cursor.rowcount > 0:
                    saved += 1
        return saved

    def run(self) -> dict:
        """Executa coletor: fetch + save + log. Retorna status dict."""
        inicio = datetime.now()
        result = {
            "source": self.source_name,
            "status": "ok",
            "fetched": 0,
            "saved": 0,
            "error": None,
        }
        try:
            records = list(self.fetch())
            result["fetched"] = len(records)
            result["saved"] = self.save_to_db(records)
        except NotImplementedError as e:
            result["status"] = "skip"
            result["error"] = "nao_implementado"
        except Exception as e:
            result["status"] = "error"
            result["error"] = f"{type(e).__name__}: {e}"

        fim = datetime.now()
        try:
            with db.connect() as conn:
                conn.execute(
                    """
                    INSERT INTO coletas_log (fonte, inicio, fim, status, registros_fetched, registros_saved, erro)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        self.source_name,
                        inicio.isoformat(),
                        fim.isoformat(),
                        result["status"],
                        result["fetched"],
                        result["saved"],
                        result["error"],
                    ),
                )
        except Exception:
            pass

        return result
