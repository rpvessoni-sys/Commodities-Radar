"""Coletor CEPEA via email subscription.

CEPEA bloqueia scraping via Cloudflare, mas oferece subscription gratuita
que envia indicadores diarios por email.

PRE-REQUISITO: usuario subscrever em https://www.cepea.esalq.usp.br/br/
(rodape "Receba indicadores por email") e criar filtro Gmail/label "cepea".

Configuracao no .env:
    CEPEA_EMAIL_LABEL=cepea          # nome da label/folder IMAP
    CEPEA_SENDER=cepea@usp.br        # sender real (ajustar quando descobrir)

Este coletor le emails via mesma infra IMAP que ja existe pro StoneX
(que esta dormente — mas a estrutura serve aqui).
"""
import os
import imaplib
import email
from email.header import decode_header
from datetime import date, datetime
import re

from .base import BaseCollector


class CepeaEmailCollector(BaseCollector):
    source_name = "cepea_email"
    cadence = "daily"
    description = "CEPEA via email subscription (parser IMAP) — substitui scraping bloqueado"
    enabled = False  # ativa quando usuario subscrever + configurar .env

    def fetch(self):
        imap_host = os.getenv("IMAP_HOST", "imap.gmail.com")
        imap_user = os.getenv("IMAP_USER", "").strip()
        imap_pass = os.getenv("IMAP_PASS", "").strip()
        cepea_sender = os.getenv("CEPEA_SENDER", "cepea").strip()

        if not (imap_user and imap_pass):
            raise NotImplementedError(
                "CEPEA email: configurar IMAP_USER, IMAP_PASS, CEPEA_SENDER no .env. "
                "Subscrever indicadores em https://www.cepea.esalq.usp.br/"
            )

        try:
            conn = imaplib.IMAP4_SSL(imap_host, 993)
            conn.login(imap_user, imap_pass)
            conn.select("INBOX")
        except Exception as e:
            return [{
                "data_referencia": date.today().isoformat(),
                "tipo": "erro",
                "commodity": "cepea",
                "metrica": "fetch_error",
                "valor": None,
                "contexto": f"IMAP login: {type(e).__name__}: {e}",
            }]

        criteria = f'(FROM "{cepea_sender}" SINCE "01-Jan-2026")'
        status, data = conn.search(None, criteria)
        if status != "OK":
            conn.close()
            conn.logout()
            return []

        ids = data[0].split()
        results = []

        for uid in ids[-10:]:  # ultimos 10 emails
            status, msg_data = conn.fetch(uid, "(RFC822)")
            if status != "OK":
                continue
            msg = email.message_from_bytes(msg_data[0][1])

            subject = self._decode_header(msg.get("Subject", ""))
            date_str = msg.get("Date", "")

            # Procura corpo texto
            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body += part.get_payload(decode=True).decode(
                            part.get_content_charset() or "utf-8", errors="replace"
                        )
            else:
                body = msg.get_payload(decode=True).decode(
                    msg.get_content_charset() or "utf-8", errors="replace"
                )

            # Parsear corpo: padrao tipico CEPEA tem linhas como
            # "Indicador Soja Paranagua: R$ XX,XX (variacao X,XX%)"
            for commodity_key, padrao in [
                ("soja", r"soja[\s\S]{0,40}?R\$\s*([\d.,]+)"),
                ("milho", r"milho[\s\S]{0,40}?R\$\s*([\d.,]+)"),
                ("boi_gordo", r"boi\s+gordo[\s\S]{0,40}?R\$\s*([\d.,]+)"),
            ]:
                m = re.search(padrao, body, re.IGNORECASE)
                if m:
                    try:
                        valor = float(m.group(1).replace(".", "").replace(",", "."))
                        results.append({
                            "data_referencia": date.today().isoformat(),
                            "tipo": "preco",
                            "commodity": commodity_key,
                            "metrica": "indicador_brl",
                            "valor": valor,
                            "unidade": "BRL",
                            "contexto": f"CEPEA email | {subject}",
                        })
                    except ValueError:
                        continue

        conn.close()
        conn.logout()
        return results

    def _decode_header(self, raw: str) -> str:
        if not raw:
            return ""
        return "".join(
            s.decode(c or "utf-8", errors="replace") if isinstance(s, bytes) else s
            for s, c in decode_header(raw)
        )
