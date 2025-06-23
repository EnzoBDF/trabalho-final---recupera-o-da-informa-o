import json
import os
from rank_bm25 import BM25Okapi

DIR = os.path.dirname(os.path.abspath(__file__))
PATH_DOCS = os.path.join(DIR, '..', '..', 'data', 'documents.txt')
PATH_QUERIES = os.path.join(DIR, '..', '..', 'data', 'queries.txt')
PATH_RESULTS = os.path.join(DIR, '..', '..', 'results', 'bm25_results.json')

def ler_documentos(path):
    docs = []
    doc_ids = []
    with open(path, encoding='utf-8') as f:
        for linha in f:
            if linha.strip():
                doc_id, conteudo = linha.strip().split('\t', 1)
                doc_ids.append(doc_id)
                docs.append(conteudo)
    return doc_ids, docs

def ler_queries(path):
    with open(path, encoding='utf-8') as f:
        return [linha.strip() for linha in f if linha.strip()]

doc_ids, documents = ler_documentos(PATH_DOCS)
tokenized_docs = [doc.lower().split() for doc in documents]
bm25 = BM25Okapi(tokenized_docs)
queries = ler_queries(PATH_QUERIES)
resultados = {}
for query in queries:
    q_tokens = query.lower().split()
    scores = bm25.get_scores(q_tokens)
    ranking = sorted(zip(doc_ids, scores), key=lambda x: x[1], reverse=True)
    resultados[query] = [doc_id for doc_id, _ in ranking]
os.makedirs(os.path.dirname(PATH_RESULTS), exist_ok=True)
with open(PATH_RESULTS, 'w', encoding='utf-8') as f:
    json.dump(resultados, f, indent=2, ensure_ascii=False)
