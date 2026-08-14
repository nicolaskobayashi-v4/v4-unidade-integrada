"""Resolve caminhos e garante o cache de texto extraído dos PDFs.

Uso nos parsers:  from _paths import BASE, TXT, CSV, garante_txt
"""
import os, subprocess, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../dados-base
TXT = os.path.join(BASE, ".txt-cache")
CSV = os.path.join(BASE, "csv")


def garante_txt():
    """Roda pdftotext -layout em todo PDF ainda sem .txt correspondente."""
    os.makedirs(TXT, exist_ok=True)
    os.makedirs(CSV, exist_ok=True)
    for nome in sorted(os.listdir(BASE)):
        if not nome.lower().endswith(".pdf"):
            continue
        destino = os.path.join(TXT, nome[:-4] + ".txt")
        if os.path.exists(destino):
            continue
        print("extraindo:", nome, file=sys.stderr)
        subprocess.run(["pdftotext", "-layout", os.path.join(BASE, nome), destino], check=True)
