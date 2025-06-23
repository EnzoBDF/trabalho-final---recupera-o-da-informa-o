from whoosh.index import open_dir
from whoosh.qparser import QueryParser
import json
import os

DIR = os.path.dirname(os.path.abspath(__file__))
PATH_QUERIES = os.path.join(DIR, '..', '..', 'data', 'queries.txt')
PATH_RESULTS = os.path.join(DIR, '..', '..', 'results', 'whoosh_results.json')

def ler_queries(path):
    with open(path, encoding='utf-8') as f:
        return [linha.strip() for linha in f if linha.strip()]

ix = open_dir('whoosh_index')
queries = ler_queries(PATH_QUERIES)
resultados = {}
with ix.searcher() as searcher:
    for query in queries:
        q = QueryParser('content', ix.schema).parse(query)
        results = searcher.search(q)
        resultados[query] = [hit['title'] for hit in results]
with open(PATH_RESULTS, 'w', encoding='utf-8') as f:
    json.dump(resultados, f, indent=2, ensure_ascii=False)