# PDF Embed — Estrategia para Relatorios em PDF

> Descoberto em 2026-05-21: 5 dos 10 relatorios mapeados usam **PDF embedado via Adobe Document Cloud**.
> O HTML wrapper baixado pelo bookmarklet NAO contem o texto do relatorio.
> Este documento define a estrategia para processar esses casos.

---

## Relatorios afetados (confirmados)

| Tipo | Nome StoneX | Cadencia |
|---|---|---|
| `panorama_mensal_oleos` | Panorama Mensal de Oleos Vegetais | Mensal |
| `resumo_usda_wasde` | Resumo do Relatorio O&D do USDA - Graos | Pos-WASDE |
| `premios_portos` | Premios nos Portos (Resumido) | Diario/Semanal |
| `fundos_diario` | Relatorio Diario de Fundos | Diario |
| `projecao_especial` | Projecao - Veiculos Eletricos no Consumo | Pontual |

Em geral, sao **relatorios analiticos longos com graficos/tabelas** que StoneX entrega como PDF.

---

## Por que o bookmarklet nao pega

Esses relatorios usam o **Adobe Document Cloud SDK** para mostrar PDF dentro de iframe:

```html
<article id="content_article" ...>
  <div id="adobe-dc-view" ...>
    <iframe src="https://documentcloud.adobe.com/view-sdk/.../iframe.html?msi=...&parent=https://stonex.digital/PATH"></iframe>
  </div>
</article>
```

O texto e renderizado pelo Adobe DC DENTRO do iframe, fora do controle da pagina. Bookmarklet pega so o HTML wrapper.

---

## Estrategias (em ordem de simplicidade)

### Estrategia 1 — Download manual do PDF (RECOMENDADO INICIO) ★
A maioria dos portais Adobe DC tem botao "Download" no proprio viewer. No StoneX:

1. Abrir o relatorio no portal
2. No viewer do PDF, clicar no botao **Download** (icone ↓ ou menu)
3. PDF salvo em Downloads
4. Mover para `commodities-radar/inbox/` (mesmo lugar que HTML)
5. Pipeline processa: precisa de **`pypdf` para extrair texto**

**Setup pra suportar PDF**:
```powershell
.\.venv\Scripts\python.exe -m pip install pypdf
```

Adicionar `pypdf>=4.0` em `system/requirements.txt`.

### Estrategia 2 — Bookmarklet v3 com captura PDF
Mais complexo: bookmarklet poderia extrair `APP.currentPDF` (variavel global do portal) e baixar direto.

```javascript
// pseudocodigo
if (window.APP && window.APP.currentPDF) {
    const pdfUrl = window.APP.currentPDF;
    fetch(pdfUrl).then(r => r.blob()).then(blob => {
        // salvar PDF
    });
}
```

Requer testar: ver se `APP.currentPDF` esta disponivel quando bookmarklet roda + se URL e acessivel sem auth adicional.

### Estrategia 3 — OCR sobre screenshot
Extremamente complexo, baixa precisao. Descartado.

---

## Implementacao Estrategia 1 (proximo passo)

1. **Instalar pypdf** no venv
2. **Criar `parse_pdf.py`** com funcao `parse_pdf(filepath) -> dict`
3. **Atualizar `ingest_stonex.watch_inbox()`** para detectar `.pdf` alem de `.html`
4. **Atualizar `_process_documents`** para chamar parse_pdf quando filename termina em .pdf
5. **Testar** com 1 PDF baixado manualmente

PDFs sao **tabelas + texto + graficos**. Texto extraivel:
- Paragrafos analiticos
- Headers de tabelas (mas valores podem perder estrutura)
- Legendas de graficos

Os graficos em si continuam imagem — sem OCR sem texto.

---

## Quando processar PDF e quando processar HTML

**HTML (parser StoneX-aware):**
- Semanal de Oleos Vegetais
- Semanal de Combustiveis
- Relatorio de Graos AM Sul
- Resumo Semanal de Commodities
- Fechamento de Cambio

**PDF (precisa pypdf):**
- Panorama Mensal de Oleos Vegetais
- Resumo USDA O&D
- Premios nos Portos
- Relatorio Diario de Fundos
- Projecoes especiais

---

## Status

- [x] Instalar pypdf no venv (v6.11)
- [x] Implementar parse_pdf.py
- [x] Atualizar ingest_stonex para detectar .pdf
- [x] Atualizar main.py para rotear HTML/PDF automaticamente
- [x] Atualizar README pra documentar fluxo dual (HTML + PDF)
- [ ] Validar com 1 PDF baixado pelo usuario
- [ ] Confirmar se botao Download do Adobe DC viewer funciona no StoneX
