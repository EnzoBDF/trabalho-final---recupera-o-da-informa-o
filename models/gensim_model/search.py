from gensim import corpora, models, similarities
import json
import os

DIR = os.path.dirname(os.path.abspath(__file__))
PATH_QUERIES = os.path.join(DIR, '..', '..', 'data', 'queries.txt')
PATH_RESULTS = os.path.join(DIR, '..', '..', 'results', 'gensim_results.json')

def ler_queries(path):
    with open(path, encoding='utf-8') as f:
        return [linha.strip() for linha in f if linha.strip()]

dictionary = corpora.Dictionary.load('gensim_dictionary.dict')
tfidf = models.TfidfModel.load('gensim_tfidf.model')
index = similarities.MatrixSimilarity.load('gensim_index.index')

queries = ler_queries(PATH_QUERIES)
resultados = {}
for query in queries:
    query_bow = dictionary.doc2bow(query.lower().split())
    sims = index[tfidf[query_bow]]
    ranking = sorted(enumerate(sims), key=lambda x: x[1], reverse=True)
    resultados[query] = [f'Doc{i+1}' for i, _ in ranking]
with open(PATH_RESULTS, 'w', encoding='utf-8') as f:
    json.dump(resultados, f, indent=2, ensure_ascii=False)