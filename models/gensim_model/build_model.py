from gensim import corpora, models, similarities
import json
import os

DIR = os.path.dirname(os.path.abspath(__file__))
PATH_DOCS = os.path.join(DIR, '..', '..', 'data', 'documents.txt')

def ler_documentos(path):
    docs = []
    with open(path, encoding='utf-8') as f:
        for linha in f:
            if linha.strip():
                _, conteudo = linha.strip().split('\t', 1)
                docs.append(conteudo)
    return docs

documents = ler_documentos(PATH_DOCS)
texts = [doc.lower().split() for doc in documents]
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
tfidf = models.TfidfModel(corpus)
index = similarities.MatrixSimilarity(tfidf[corpus])

dictionary.save("gensim_dictionary.dict")
tfidf.save("gensim_tfidf.model")
index.save("gensim_index.index")
