#!/usr/bin/env python3
"""Afinidade entre marcas — quem compra A também compra B?

Gera (1) o bloco `brand_affinity` para ee-s3-pdv-base-ativa.json e (2) os CSVs de
público por oportunidade de cross-sell.

Métrica principal é o LIFT, não a co-compra bruta: numa base onde a Altenburg tem
36% de penetração, qualquer marca "co-ocorre" muito com ela por puro tamanho.
lift = P(B|A) / P(B) corrige isso — 1,0 é o acaso, acima disso é afinidade real.
"""
import csv, itertools, json, os
from _paths import CSV

MARCAS = ["ALTENBURG", "NIAZITEX", "BUDDEMEYER", "KACYUMARA", "KARSTEN",
          "BELLA JANELA", "TRUSSARDI", "BUDD LUXUS", "PLUMASSUL"]
COL = {m: "m_" + m.lower().replace(" ", "_") for m in MARCAS}

MIN_CO = 100          # co-compradores mínimos para o par ser reportado
# Regra de geração de lista de público. Deliberadamente restritiva: com lift >= 1,5
# qualificam 35 pares, o que devolve quase toda a base em 35 arquivos de dado pessoal
# e anula a priorização. O corte em 2,5 fica com os pares de afinidade inequívoca.
MIN_LIFT_PUB = 2.5
MIN_VALOR_PUB = 2_000_000
AMOSTRA_PEQUENA = 500  # marcas abaixo disso têm lift instável


def main():
    rows = list(csv.DictReader(open(os.path.join(CSV, "clientes-consolidado.csv"), encoding="utf-8-sig")))
    byc = {r["codigo"]: r for r in rows}
    N = len(rows)
    own = {m: {r["codigo"] for r in rows if r[COL[m]] == "1"} for m in MARCAS}

    def valor(cods):
        return sum(float(byc[c]["total"]) for c in cods if byc[c]["total"])

    def com_zap(cods):
        return sum(1 for c in cods if byc[c]["whatsapp"])

    # ---------- matriz
    matrix = []
    for a in MARCAS:
        linha = {"marca": a, "base": len(own[a]),
                 "amostra_pequena": len(own[a]) < AMOSTRA_PEQUENA, "pares": []}
        for b in MARCAS:
            if a == b:
                continue
            inter = own[a] & own[b]
            pba = len(inter) / len(own[a])
            lift = pba / (len(own[b]) / N)
            linha["pares"].append({
                "marca": b, "co_compradores": len(inter),
                "p_b_dado_a": round(pba, 4), "lift": round(lift, 2),
                "confiavel": len(inter) >= MIN_CO})
        linha["pares"].sort(key=lambda p: -p["lift"])
        matrix.append(linha)

    # ---------- oportunidades direcionais
    ops = []
    for a, b in itertools.permutations(MARCAS, 2):
        A, B = own[a], own[b]
        inter, gap = A & B, A - B
        if len(inter) < MIN_CO or not gap:
            continue
        lift = (len(inter) / len(A)) / (len(B) / N)
        ops.append({
            "de": a, "ofertar": b, "lift": round(lift, 2),
            "base_de": len(A), "ja_compram_ambas": len(inter),
            "p_b_dado_a": round(len(inter) / len(A), 4),
            "gap_clientes": len(gap), "gap_valor": round(valor(gap), 2),
            "gap_com_whatsapp": com_zap(gap),
            "amostra_pequena": len(A) < AMOSTRA_PEQUENA or len(B) < AMOSTRA_PEQUENA,
            "_gap": gap})
    ops.sort(key=lambda o: -o["lift"])

    # ---------- clusters: quem se puxa e quem é ilha
    lift_medio = {}
    for a in MARCAS:
        ls = [p["lift"] for p in next(l for l in matrix if l["marca"] == a)["pares"]]
        lift_medio[a] = round(sum(ls) / len(ls), 2)
    ilhas = [m for m in MARCAS if lift_medio[m] < 1.15]
    cluster = sorted([m for m in MARCAS if lift_medio[m] >= 1.8], key=lambda m: -lift_medio[m])

    # ---------- Bella Janela: o caso da ilha
    bj = next(l for l in matrix if l["marca"] == "BELLA JANELA")
    bj_abaixo = [p for p in bj["pares"] if p["lift"] <= 1.0]

    # ---------- segmento sem marca
    sem = [r["codigo"] for r in rows if r["n_marcas"] == "0"]

    bloco = {
        "metodo": (
            "Co-ocorrência de compra por marca sobre 31.991 clientes, no período de 31 meses. "
            "A métrica de ranqueamento é o LIFT (P(B|A) ÷ P(B)), não a co-compra bruta: com a "
            "Altenburg em 36% da base, qualquer marca co-ocorre muito com ela por puro tamanho. "
            "Lift 1,0 é o acaso; acima disso há afinidade real. Só são reportados pares com pelo "
            f"menos {MIN_CO} co-compradores."),
        "matrix": matrix,
        "lift_medio_por_marca": lift_medio,
        "top_opportunities": [{k: v for k, v in o.items() if k != "_gap"} for o in ops[:15]],
        "total_oportunidades": len(ops),
        "clusters": {
            "premium_interligado": {
                "marcas": cluster,
                "leitura": (
                    "Essas marcas se puxam entre si com lift de 2,6 a 4,75. Quem compra uma tem "
                    "de 2,6 a 4,8 vezes mais chance de comprar a outra do que um cliente aleatório. "
                    "Aqui o cross-sell é oferta direta: o cliente já demonstrou o comportamento.")},
            "ilhas": {
                "marcas": ilhas,
                "leitura": (
                    "Marcas cujo comprador não migra para o resto da loja. Não adianta ofertar — "
                    "precisa de ponte desenhada: motivo, ocasião e combinação explícita.")}},
        "bella_janela_alert": {
            "headline": (
                "Bella Janela é uma ilha: em 6 dos 8 cruzamentos o lift fica em 1,00 ou abaixo — "
                "comprar Bella Janela não aumenta em nada a chance de comprar qualquer outra marca."),
            "lift_medio": lift_medio["BELLA JANELA"],
            "pares_no_acaso_ou_abaixo": [{"marca": p["marca"], "lift": p["lift"]} for p in bj_abaixo],
            "base": len(own["BELLA JANELA"]),
            "so_what": (
                "É a prova quantificada da dor que o próprio cliente descreveu no kick-off: o "
                "produto-isca de margem quase zero (cortina a partir de R$ 99) atrai gente que "
                "compra só aquilo e nunca sobe de mix. A isca funciona para gerar fluxo e falha "
                "como porta de entrada. Corrigir isso é desenhar a segunda compra na própria venda "
                "da cortina, não mandar oferta depois.")},
        "no_brand_segment": {
            "clientes": len(sem), "valor": round(valor(sem), 2), "com_whatsapp": com_zap(sem),
            "gasto_medio": round(valor(sem) / len(sem), 2),
            "leitura": (
                "Clientes que não aparecem em nenhuma das 9 marcas exportadas. Gasto médio muito "
                "abaixo da base e concentração de compra única — é a cauda de compra avulsa de item "
                "barato ou sem marca cadastrada. Volume grande e contatável, valor unitário baixo: "
                "serve para campanha de alcance, não para oferta premium.")},
        "strategy": [
            {"publico": "Cluster premium — compradores de uma marca premium sem as outras",
             "acao": "Oferta direta da marca irmã, com o argumento de composição (mesma cama, mesma linha).",
             "por_que": "Lift de 2,6 a 4,75: o comportamento já existe, só não foi provocado.",
             "esforco": "baixo"},
            {"publico": "Compradores de Bella Janela (cortina) — 4.753 clientes",
             "acao": "Ponte desenhada no PDV: ao vender a cortina, montar o ambiente (cortina + almofada + tapete) como sugestão, não como oferta posterior.",
             "por_que": "Lift ≤1,0 contra quase tudo. Oferta isolada por WhatsApp tende a não converter — o cliente não se enxerga comprando o resto.",
             "esforco": "medio"},
            {"publico": "Base Altenburg — 11.471 clientes, a maior da loja",
             "acao": "Usar como base de alcance e não de afinidade: campanhas amplas, sazonais, de renovação.",
             "por_que": "Lift uniformemente baixo (1,31 a 1,59) com todas as marcas. É a marca que todo mundo compra, não um sinal de perfil.",
             "esforco": "baixo"},
            {"publico": "9.591 clientes sem nenhuma das 9 marcas",
             "acao": "Primeiro entender o que compraram — depende da árvore de categorias (pendência 2.6 com o Anderson).",
             "por_que": "Sem saber o que levaram, qualquer oferta é chute.",
             "esforco": "bloqueado"}],
    }

    # ---------- CSVs de público
    pub_dir = os.path.join(CSV, "publicos")
    os.makedirs(pub_dir, exist_ok=True)
    gerados = []
    for o in ops:
        if o["lift"] < MIN_LIFT_PUB or o["gap_valor"] < MIN_VALOR_PUB:
            continue
        nome = f"publico_{o['de'].replace(' ','-')}_para_{o['ofertar'].replace(' ','-')}.csv"
        alvo = sorted(o["_gap"], key=lambda c: -float(byc[c]["total"] or 0))
        with open(os.path.join(pub_dir, nome), "w", newline="", encoding="utf-8-sig") as f:
            w = csv.writer(f)
            w.writerow(["codigo", "nome", "cidade", "whatsapp", "total", "ticket_medio", "marcas_atuais"])
            for c in alvo:
                r = byc[c]
                w.writerow([r["codigo"], r["nome"], r["cidade"], r["whatsapp"],
                            r["total"], r["ticket_medio"], r["marcas"]])
        gerados.append({"arquivo": nome, "de": o["de"], "ofertar": o["ofertar"],
                        "lift": o["lift"], "clientes": len(alvo),
                        "valor": o["gap_valor"], "com_whatsapp": o["gap_com_whatsapp"]})

    # segmento sem marca
    with open(os.path.join(pub_dir, "publico_SEM-MARCA.csv"), "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["codigo", "nome", "cidade", "whatsapp", "total", "ticket_medio"])
        for c in sorted(sem, key=lambda c: -float(byc[c]["total"] or 0)):
            r = byc[c]
            w.writerow([r["codigo"], r["nome"], r["cidade"], r["whatsapp"], r["total"], r["ticket_medio"]])
    gerados.append({"arquivo": "publico_SEM-MARCA.csv", "de": "—", "ofertar": "—",
                    "lift": None, "clientes": len(sem), "valor": round(valor(sem), 2),
                    "com_whatsapp": com_zap(sem)})
    bloco["audience_files"] = {
        "diretorio": "base-de-conhecimento/dados-base/csv/publicos/",
        "regra": f"lift >= {MIN_LIFT_PUB} E valor do gap >= R$ {MIN_VALOR_PUB:,.0f}".replace(",", "."),
        "arquivos": gerados,
        "aviso_lgpd": (
            "Contêm nome, cidade e telefone de clientes identificados. Estão prontos para uso, mas a "
            "base legal de contato segue em aberto (pendência 3.2 com o Anderson). Não disparar antes "
            "disso.")}

    saida = os.path.join(os.path.dirname(os.path.abspath(__file__)), "brand_affinity.json")
    json.dump(bloco, open(saida, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    # ---------- validação
    print(f"clientes: {N}  ·  pares reportáveis: {len(ops)}")
    print(f"lift médio por marca: " + " · ".join(f"{m}={lift_medio[m]}" for m in MARCAS))
    print(f"cluster interligado: {cluster}")
    print(f"ilhas: {ilhas}")
    print(f"\npúblicos gerados: {len(gerados)} arquivos em {pub_dir}")
    for g in gerados:
        print(f"  {g['arquivo']:<52} {g['clientes']:>6,} cli  R$ {g['valor']:>12,.0f}  zap {g['com_whatsapp']:>6,}")

    print("\n--- checagens ---")
    sim = all(len(own[a] & own[b]) == len(own[b] & own[a]) for a, b in itertools.combinations(MARCAS, 2))
    print(f"  interseção simétrica |A∩B|==|B∩A|: {'OK' if sim else 'FALHOU'}")
    err = [(a, b) for a, b in itertools.combinations(MARCAS, 2)
           if abs(((len(own[a] & own[b]) / len(own[a])) / (len(own[b]) / N))
                  - ((len(own[a] & own[b]) / len(own[b])) / (len(own[a]) / N))) > 1e-9]
    print(f"  lift(A→B)==lift(B→A): {'OK' if not err else f'FALHOU em {err}'}")
    marcas_csv = {}
    for r in csv.DictReader(open(os.path.join(CSV, "clientes-por-marca.csv"), encoding="utf-8-sig")):
        marcas_csv.setdefault(r["marca"], set()).add(r["codigo"])
    dif = [(m, len(own[m]), len(marcas_csv.get(m, ()))) for m in MARCAS if len(own[m]) != len(marcas_csv.get(m, ()))]
    print(f"  base por marca bate com clientes-por-marca.csv: {'OK' if not dif else dif}")


main()


def tier_carteira():
    """Escada de gasto acumulado + público do topo tratável como carteira.

    Complementa (e corrige) a leitura de 'negócio de volume': a base é de volume,
    mas existe um topo pequeno o bastante para acompanhamento nomeado.
    """
    rows = [r for r in csv.DictReader(open(os.path.join(CSV, "clientes-consolidado.csv"), encoding="utf-8-sig"))
            if r["na_curva_abc"] == "1"]
    for r in rows:
        r["t"] = float(r["total"])
    TOT, N = sum(r["t"] for r in rows), len(rows)
    VENDEDORAS = 8  # as que concentram carteira exclusiva relevante

    escada = []
    for corte in (20000, 10000, 5000, 3000, 2000):
        sel = [r for r in rows if r["t"] >= corte]
        s = sum(r["t"] for r in sel)
        escada.append({"corte": corte, "clientes": len(sel), "pct_base": round(len(sel) / N, 4),
                       "receita": round(s, 2), "pct_receita": round(s / TOT, 4),
                       "gasto_medio": round(s / len(sel), 2)})

    CORTE = 5000
    tier = sorted([r for r in rows if r["t"] >= CORTE], key=lambda r: -r["t"])
    zap = sum(1 for r in tier if r["whatsapp"])
    uma = sum(1 for r in tier if r["qtde"] == "1")
    receita = sum(r["t"] for r in tier)

    with open(os.path.join(CSV, "publicos", "publico_TOP-CARTEIRA.csv"), "w",
              newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["codigo", "nome", "cidade", "whatsapp", "total", "qtde", "ticket_medio",
                    "n_marcas", "marcas", "vendedores"])
        for r in tier:
            w.writerow([r["codigo"], r["nome"], r["cidade"], r["whatsapp"], r["total"],
                        r["qtde"], r["ticket_medio"], r["n_marcas"], r["marcas"], r["vendedores"]])

    bloco = {
        "headline": (f"{len(tier):,} clientes gastaram R$ {CORTE:,} ou mais e fazem "
                     f"{receita/TOT:.1%} da receita — {zap/len(tier):.0%} têm celular no cadastro "
                     f"e hoje não recebem tratamento nenhum de carteira.").replace(",", "."),
        "corte": CORTE, "clientes": len(tier), "pct_base": round(len(tier) / N, 4),
        "receita": round(receita, 2), "pct_receita": round(receita / TOT, 4),
        "gasto_medio": round(receita / len(tier), 2),
        "com_whatsapp": zap, "compra_unica": uma,
        "por_vendedora": round(len(tier) / VENDEDORAS),
        "escada": escada,
        "leitura": (
            "A base é de volume, mas o topo é de carteira. Os 10.386 clientes que formam 80% da "
            "receita só se movem por campanha ampla e processo padronizado — ninguém gerencia dez mil "
            "relacionamentos. Já estes clientes são poucos o bastante para acompanhamento nomeado: "
            f"divididos entre as {VENDEDORAS} vendedoras com carteira exclusiva relevante, dão cerca "
            f"de {round(len(tier)/VENDEDORAS)} clientes cada. Hoje eles estão diluídos em territórios "
            "de 2.400 a 3.600 pessoas e não recebem acompanhamento diferenciado."),
        "por_que_agora": (
            f"Apenas {uma/len(tier):.0%} deste grupo comprou uma única vez — é gente que já volta "
            "sozinha. O custo de mantê-los é baixo e o risco de perdê-los por desatenção é real, "
            "porque nada no processo atual sinaliza que são diferentes."),
        "arquivo": "publicos/publico_TOP-CARTEIRA.csv",
    }
    saida = os.path.join(os.path.dirname(os.path.abspath(__file__)), "key_accounts_tier.json")
    json.dump(bloco, open(saida, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    print("\n=== TIER DE CARTEIRA ===")
    print(f"{'corte':>10} {'clientes':>9} {'% base':>7} {'receita':>14} {'% rec':>7} {'gasto médio':>12}")
    for e in escada:
        print(f"R$ {e['corte']:>7,} {e['clientes']:>9,} {e['pct_base']:>6.1%} "
              f"R$ {e['receita']:>12,.0f} {e['pct_receita']:>6.1%} R$ {e['gasto_medio']:>9,.0f}")
    print(f"\ntier escolhido (>= R$ {CORTE:,}): {len(tier):,} clientes · {zap:,} com whatsapp "
          f"({zap/len(tier):.0%}) · {uma:,} de compra única ({uma/len(tier):.0%}) "
          f"· ~{round(len(tier)/VENDEDORAS)} por vendedora")


tier_carteira()
