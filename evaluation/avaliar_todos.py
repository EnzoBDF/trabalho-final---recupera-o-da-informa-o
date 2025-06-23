import json
import os
from metrics import calcular_metrica

DIR = os.path.dirname(os.path.abspath(__file__))
PATH_RELEVANCIA = os.path.join(DIR, '..', 'data', 'relevancia.json')
MODELOS = [
    ("BM25", os.path.join(DIR, '..', 'results', 'bm25_results.json')),
    ("Gensim", os.path.join(DIR, '..', 'results', 'gensim_results.json')),
    ("Whoosh", os.path.join(DIR, '..', 'results', 'whoosh_results.json'))
]

if not os.path.exists(PATH_RELEVANCIA):
    print(f"[ERRO] Arquivo de relevância não encontrado: {PATH_RELEVANCIA}")
    exit(1)

with open(PATH_RELEVANCIA, encoding="utf-8") as f:
    relevantes = json.load(f)

for nome, caminho in MODELOS:
    if not os.path.exists(caminho):
        print(f"[AVISO] Resultados não encontrados para {nome}: {caminho}")
        continue
    with open(caminho, encoding="utf-8") as f:
        resultados = json.load(f)
    print(f"\n=== {nome} ===")
    precs, recs, f1s = [], [], []
    for query, docs in resultados.items():
        rel = relevantes.get(query, [])
        precisao, revocacao, f1 = calcular_metrica(docs, rel)
        precs.append(precisao)
        recs.append(revocacao)
        f1s.append(f1)
        print(f"Query: {query}")
        print(f"  Precisão: {precisao:.2f} | Revocação: {revocacao:.2f} | F1: {f1:.2f}")
    if precs:
        print(f"Média - Precisão: {sum(precs)/len(precs):.2f} | Revocação: {sum(recs)/len(recs):.2f} | F1: {sum(f1s)/len(f1s):.2f}") 