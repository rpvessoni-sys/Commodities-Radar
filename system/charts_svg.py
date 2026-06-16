# -*- coding: utf-8 -*-
"""Gerador de graficos SVG inline para o relatorio HTML (tema dark).

100% stdlib, funcoes puras: entram dados, sai string SVG (ou "" nos casos
degenerados — nunca crasha). Cores sempre via variaveis CSS do relatorio
(--accent, --muted, --border, --warn, --bull, --bear), entao o SVG herda
o tema do HTML que o embute.

Formatacao de valores e responsabilidade de quem chama (fmt_valor);
aqui nao se usa locale nem formato pt-BR.
"""
import html
import math
from datetime import date

# fatores "bonitos" de passo de eixo (multiplicar por 10^n)
_NICE_FATORES = (1.0, 2.0, 2.5, 5.0)
# cortes geometricos entre fatores consecutivos: sqrt(a*b)
_NICE_CORTES = (1.4142135, 2.2360679, 3.5355339, 7.0710678)


def _num(x):
    """Formata coordenada SVG com ate 2 casas, sem zeros a direita."""
    s = "{:.2f}".format(float(x))
    s = s.rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


def _passo_bonito(bruto):
    """Passo 'redondo' (1/2/2.5/5 x 10^n) mais proximo do passo bruto."""
    if bruto <= 0:
        return 1.0
    exp = math.floor(math.log10(bruto))
    frac = bruto / (10.0 ** exp)
    for corte, fator in zip(_NICE_CORTES, _NICE_FATORES):
        if frac < corte:
            return fator * (10.0 ** exp)
    return 10.0 * (10.0 ** exp)


def _ticks(vmin, vmax, alvo=4):
    """Lista de ~alvo ticks em numeros redondos dentro de [vmin, vmax]."""
    passo = _passo_bonito((vmax - vmin) / float(alvo))
    k0 = int(math.ceil(vmin / passo - 1e-9))
    k1 = int(math.floor(vmax / passo + 1e-9))
    return [k * passo for k in range(k0, k1 + 1)]


def _dominio_y(valores, niveis=None, pad_frac=0.03):
    """Range do eixo Y: dados + niveis, com folga de pad_frac nas pontas."""
    vs = list(valores)
    if niveis:
        vs.extend(float(v) for v in niveis.values())
    vmin, vmax = min(vs), max(vs)
    if vmax == vmin:
        folga = max(1.0, abs(vmin) * 0.05)
        return vmin - folga, vmax + folga
    pad = (vmax - vmin) * pad_frac
    return vmin - pad, vmax + pad


def _parse_iso(s):
    """Data ISO -> date, ou None se nao parsear."""
    try:
        return date.fromisoformat(str(s)[:10])
    except (ValueError, TypeError):
        return None


def _fmt_data(s, curto):
    """Label de data do eixo X: DD/MM (serie curta) ou MM/AA."""
    d = _parse_iso(s)
    if d is None:
        return html.escape(str(s))
    if curto:
        return "{:02d}/{:02d}".format(d.day, d.month)
    return "{:02d}/{:02d}".format(d.month, d.year % 100)


def _fmt_eixo_padrao(v):
    """Formato default dos labels de eixo (simples, nao pt-BR)."""
    return "{:,.0f}".format(v)


def _fmt_spread(v):
    """Valor de spread com sinal explicito, sem zeros inuteis."""
    s = "{:+.2f}".format(v)
    if "." in s:
        s = s.rstrip("0").rstrip(".")
    return s


def sparkline(valores, width=130, height=34, cor="var(--accent)"):
    """Mini-linha de KPI: sem eixos, sem labels, circulo no ultimo ponto.

    valores podem conter None (sao filtrados). Retorna "" se sobrarem
    menos de 2 valores ou se o range for zero.
    """
    vals = [float(v) for v in (valores or []) if v is not None]
    if len(vals) < 2:
        return ""
    vmin, vmax = min(vals), max(vals)
    if vmax == vmin:
        return ""
    pad = 3.0
    pw, ph = width - 2 * pad, height - 2 * pad
    n = len(vals)
    pts = []
    for i, v in enumerate(vals):
        x = pad + pw * i / (n - 1)
        y = pad + ph * (1.0 - (v - vmin) / (vmax - vmin))
        pts.append("{},{}".format(_num(x), _num(y)))
    cor_e = html.escape(str(cor), quote=True)
    ux, uy = pts[-1].split(",")
    return (
        '<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
        'xmlns="http://www.w3.org/2000/svg">'
        '<g opacity="0.9">'
        '<polyline points="{p}" fill="none" stroke="{c}" stroke-width="1.5" '
        'stroke-linejoin="round" stroke-linecap="round"/>'
        '<circle cx="{cx}" cy="{cy}" r="2.5" fill="{c}"/>'
        "</g></svg>"
    ).format(w=int(width), h=int(height), p=" ".join(pts), c=cor_e, cx=ux, cy=uy)


def line_chart(serie, width=720, height=220, niveis=None, label_y="",
               cor="var(--accent)", fmt_valor=None):
    """Grafico de linha com area, gridlines, niveis tracejados e anotacao.

    serie: [(data_iso_str, float), ...] em ordem cronologica crescente;
    pontos com valor None sao filtrados. Retorna "" com menos de 2 pontos.
    niveis: dict rotulo -> valor; vira linha horizontal tracejada (--warn)
    e expande o range do eixo Y se estiver fora dele.
    fmt_valor: callable float -> str para labels do eixo Y e ultimo valor.
    label_y: texto vertical opcional na margem esquerda.
    """
    pontos = [(d, float(v)) for d, v in (serie or []) if v is not None]
    if len(pontos) < 2:
        return ""
    if fmt_valor is None:
        fmt_valor = _fmt_eixo_padrao

    m_esq, m_dir, m_topo, m_base = 56, 64, 14, 22
    pw = width - m_esq - m_dir
    ph = height - m_topo - m_base
    base_y = m_topo + ph

    vals = [v for _, v in pontos]
    vmin, vmax = _dominio_y(vals, niveis)
    n = len(pontos)

    def _x(i):
        return m_esq + pw * i / (n - 1)

    def _y(v):
        return m_topo + ph * (1.0 - (v - vmin) / (vmax - vmin))

    cor_e = html.escape(str(cor), quote=True)
    partes = [
        '<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
        'xmlns="http://www.w3.org/2000/svg">'.format(w=int(width), h=int(height))
    ]

    # gridlines horizontais + labels do eixo Y
    for t in _ticks(vmin, vmax):
        yt = _num(_y(t))
        partes.append(
            '<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" '
            'stroke="var(--border)" stroke-width="1" opacity="0.6"/>'.format(
                x1=m_esq, x2=m_esq + pw, y=yt))
        partes.append(
            '<text x="{x}" y="{y}" text-anchor="end" font-size="10" '
            'fill="var(--muted)">{t}</text>'.format(
                x=m_esq - 8, y=_num(_y(t) + 3), t=html.escape(str(fmt_valor(t)))))

    coords = [(_x(i), _y(v)) for i, (_, v) in enumerate(pontos)]

    # area sob a linha
    caminho = ["M{},{}".format(_num(coords[0][0]), _num(base_y))]
    for cx, cy in coords:
        caminho.append("L{},{}".format(_num(cx), _num(cy)))
    caminho.append("L{},{} Z".format(_num(coords[-1][0]), _num(base_y)))
    partes.append('<path d="{d}" fill="{c}" opacity="0.08" stroke="none"/>'.format(
        d=" ".join(caminho), c=cor_e))

    # niveis (suporte/resistencia/etc): tracejado + rotulo a direita
    for rotulo, valor in (niveis or {}).items():
        yn = _num(_y(float(valor)))
        partes.append(
            '<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="var(--warn)" '
            'stroke-width="1" stroke-dasharray="5 3" opacity="0.8"/>'.format(
                x1=m_esq, x2=m_esq + pw, y=yn))
        partes.append(
            '<text x="{x}" y="{y}" text-anchor="end" font-size="10" '
            'fill="var(--warn)">{r}</text>'.format(
                x=_num(m_esq + pw - 2), y=_num(_y(float(valor)) - 4),
                r=html.escape(str(rotulo))))

    # linha principal
    pts_str = " ".join("{},{}".format(_num(cx), _num(cy)) for cx, cy in coords)
    partes.append(
        '<polyline points="{p}" fill="none" stroke="{c}" stroke-width="2" '
        'stroke-linejoin="round" stroke-linecap="round"/>'.format(
            p=pts_str, c=cor_e))

    # ultimo ponto: circulo + valor anotado a direita
    ux, uy = coords[-1]
    partes.append('<circle cx="{cx}" cy="{cy}" r="3" fill="{c}"/>'.format(
        cx=_num(ux), cy=_num(uy), c=cor_e))
    partes.append(
        '<text x="{x}" y="{y}" font-size="11" font-weight="600" '
        'fill="{c}">{t}</text>'.format(
            x=_num(ux + 6), y=_num(uy + 4), c=cor_e,
            t=html.escape(str(fmt_valor(pontos[-1][1])))))

    # eixo X: ~5-6 labels de data espacados uniformemente
    d0, d1 = _parse_iso(pontos[0][0]), _parse_iso(pontos[-1][0])
    curto = bool(d0 and d1 and (d1 - d0).days < 120)
    n_lab = min(6, n)
    idxs = sorted({int(round(k * (n - 1) / float(n_lab - 1)))
                   for k in range(n_lab)})
    for i in idxs:
        partes.append(
            '<text x="{x}" y="{y}" text-anchor="middle" font-size="10" '
            'fill="var(--muted)">{t}</text>'.format(
                x=_num(_x(i)), y=base_y + 16, t=_fmt_data(pontos[i][0], curto)))

    # label vertical opcional do eixo Y
    if label_y:
        cy_rot = m_topo + ph / 2.0
        partes.append(
            '<text transform="rotate(-90)" x="{x}" y="12" text-anchor="middle" '
            'font-size="10" fill="var(--muted)">{t}</text>'.format(
                x=_num(-cy_rot), t=html.escape(str(label_y))))

    partes.append("</svg>")
    return "".join(partes)


def bar_spread(items, width=320, height=120):
    """Barras horizontais de spreads (tipicamente 3-8 vencimentos).

    items: [(rotulo_str, valor_float), ...]; valores None sao filtrados.
    Positivo = var(--bull), negativo = var(--bear). Havendo negativos o
    zero fica no centro da area de barras; senao partem da esquerda.
    Retorna "" sem itens validos.
    """
    dados = [(str(r), float(v)) for r, v in (items or []) if v is not None]
    if not dados:
        return ""

    label_w = 58
    bx0 = label_w + 6
    bx1 = width - 4
    bw = bx1 - bx0
    pad_valor = 32  # espaco reservado pro texto na ponta da barra
    tem_neg = any(v < 0 for _, v in dados)
    max_abs = max(abs(v) for _, v in dados) or 1.0
    n = len(dados)
    row_h = height / float(n)
    bar_h = max(4.0, min(14.0, row_h - 8))

    partes = [
        '<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
        'xmlns="http://www.w3.org/2000/svg">'.format(w=int(width), h=int(height))
    ]

    if tem_neg:
        x_zero = bx0 + bw / 2.0
        escala = (bw / 2.0 - pad_valor) / max_abs
        partes.append(
            '<line x1="{x}" y1="2" x2="{x}" y2="{y}" stroke="var(--border)" '
            'stroke-width="1"/>'.format(x=_num(x_zero), y=int(height) - 2))
    else:
        x_zero = float(bx0)
        escala = (bw - pad_valor) / max_abs

    for i, (rotulo, v) in enumerate(dados):
        cy = (i + 0.5) * row_h
        comp = abs(v) * escala
        if v >= 0:
            bar_x, fill = x_zero, "var(--bull)"
            tx, anchor = x_zero + comp + 4, "start"
        else:
            bar_x, fill = x_zero - comp, "var(--bear)"
            tx, anchor = x_zero - comp - 4, "end"
        partes.append(
            '<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2" '
            'fill="{f}" opacity="0.75"/>'.format(
                x=_num(bar_x), y=_num(cy - bar_h / 2.0),
                w=_num(comp), h=_num(bar_h), f=fill))
        partes.append(
            '<text x="{x}" y="{y}" text-anchor="end" font-size="10" '
            'fill="var(--muted)">{t}</text>'.format(
                x=label_w, y=_num(cy + 3), t=html.escape(rotulo)))
        partes.append(
            '<text x="{x}" y="{y}" text-anchor="{a}" font-size="10" '
            'fill="var(--text)">{t}</text>'.format(
                x=_num(tx), y=_num(cy + 3), a=anchor,
                t=html.escape(_fmt_spread(v))))

    partes.append("</svg>")
    return "".join(partes)
