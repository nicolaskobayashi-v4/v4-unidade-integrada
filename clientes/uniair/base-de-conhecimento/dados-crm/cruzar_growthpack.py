#!/usr/bin/env python3
"""
Rotina mensal: cruza contatos_vendas.csv com o CSV mais recente do Growth Pack
por telefone (últimos 8 dígitos, ignorando o nono dígito do WhatsApp) e gera
contatos_vendas_enriquecido.csv com as colunas do Growth Pack preenchidas
quando houver match (em branco quando não houver).

Uso: python3 cruzar_growthpack.py
"""
import csv
import glob
import os
import re

from dateutil import parser as dtparser

PASTA = os.path.dirname(os.path.abspath(__file__))
CONTATOS_VENDAS = os.path.join(PASTA, "contatos_vendas.csv")
SAIDA = os.path.join(PASTA, "contatos_vendas_enriquecido.csv")

# Colunas do Growth Pack que são sempre vazias no export (cabeçalho sem nome)
COLUNAS_VAZIAS_IGNORAR = {""}

# Alguns leads do Growth Pack têm o telefone_Whatsapp quebrado (ex.: "#ERROR!",
# bug de fórmula na planilha de origem) e por isso nunca casam pelo telefone.
# Quando confirmamos manualmente (por e-mail) que é o mesmo contato e que ele
# veio de mídia paga (está na base do Growth Pack, mesmo sem UTM capturada),
# registramos aqui para o match continuar valendo nas próximas rodadas.
# Contato (como aparece em contatos_vendas.csv) -> e-mail do lead no Growth Pack
MATCHES_MANUAIS_POR_EMAIL = {
    "Soca": "soca@viaporto.com.br",
}


def encontrar_csv_growthpack():
    candidatos = [
        f for f in glob.glob(os.path.join(PASTA, "GrowthPack*Base de Leads*.csv"))
        if not f.endswith(os.path.basename(SAIDA))
    ]
    if not candidatos:
        raise FileNotFoundError(
            f"Nenhum CSV do Growth Pack encontrado em {PASTA} "
            "(esperado algo como 'GrowthPack _ Uniair - Base de Leads (N).csv')"
        )
    candidatos.sort(key=os.path.getmtime, reverse=True)
    return candidatos[0]


def chave_telefone(telefone):
    """Últimos 8 dígitos do telefone, robusto à presença/ausência do 9º dígito."""
    digitos = re.sub(r"\D", "", telefone or "")
    if len(digitos) < 8:
        return None
    return digitos[-8:]


def parse_data(valor):
    try:
        return dtparser.parse(valor, dayfirst=True)
    except (ValueError, TypeError):
        return None


def carregar_growthpack(caminho):
    with open(caminho, encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        colunas = [h for h in header if h not in COLUNAS_VAZIAS_IGNORAR]
        idx_colunas = [i for i, h in enumerate(header) if h not in COLUNAS_VAZIAS_IGNORAR]
        idx_telefone = header.index("telefone_Whatsapp")
        idx_email = header.index("E_mail")
        idx_data = header.index("Data da Conversão")

        indice_tel = {}
        indice_email = {}
        for linha in reader:
            registro = {colunas[j]: linha[idx_colunas[j]] for j in range(len(colunas))}
            data = parse_data(linha[idx_data])

            chave = chave_telefone(linha[idx_telefone])
            if chave is not None:
                indice_tel.setdefault(chave, []).append((data, registro))

            email = (linha[idx_email] or "").strip().lower()
            if email:
                indice_email.setdefault(email, []).append((data, registro))

    def escolher_mais_antigo(ocorrencias):
        com_data = [o for o in ocorrencias if o[0] is not None]
        if com_data:
            com_data.sort(key=lambda o: o[0])
            return com_data[0][1]
        return ocorrencias[0][1]

    escolhidos_tel = {chave: escolher_mais_antigo(ocs) for chave, ocs in indice_tel.items()}
    escolhidos_email = {email: escolher_mais_antigo(ocs) for email, ocs in indice_email.items()}

    return colunas, escolhidos_tel, escolhidos_email


def main():
    caminho_growthpack = encontrar_csv_growthpack()
    print(f"Usando Growth Pack: {os.path.basename(caminho_growthpack)}")

    colunas_gp, indice_tel, indice_email = carregar_growthpack(caminho_growthpack)
    colunas_saida = ["Contato", "Telefone", "Fechada em", "Venda (R$)"] + colunas_gp + ["Match_GrowthPack"]

    with open(CONTATOS_VENDAS, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        contatos = list(reader)

    total, com_match, manuais = 0, 0, 0

    with open(SAIDA, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=colunas_saida)
        writer.writeheader()
        for linha in contatos:
            total += 1
            chave = chave_telefone(linha.get("Telefone"))
            registro_gp = indice_tel.get(chave) if chave else None
            origem_match = "Telefone" if registro_gp else ""

            if registro_gp is None:
                email_manual = MATCHES_MANUAIS_POR_EMAIL.get(linha.get("Contato"))
                if email_manual:
                    registro_gp = indice_email.get(email_manual.lower())
                    if registro_gp:
                        origem_match = "Manual (telefone com erro na planilha)"
                        manuais += 1

            saida = dict(linha)
            if registro_gp:
                com_match += 1
                saida.update(registro_gp)
            else:
                saida.update({col: "" for col in colunas_gp})
            saida["Match_GrowthPack"] = origem_match
            writer.writerow(saida)

    print(f"Total de contatos: {total}")
    print(f"Com match no Growth Pack: {com_match} (dos quais {manuais} manual/e-mail)")
    print(f"Sem match: {total - com_match}")
    print(f"Saída gravada em: {SAIDA}")


if __name__ == "__main__":
    main()
