from gensim import corpora, models, similarities
import json

documents = [
    "Os gatos domésticos são amigáveis e carinhosos.",
    "Felinos selvagens vivem em florestas e são caçadores.",
    "Os cães também são animais domésticos muito leais."
]
texts = [doc.lower().split() for doc in documents]
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
tfidf = models.TfidfModel(corpus)
index = similarities.MatrixSimilarity(tfidf[corpus])

dictionary.save("gensim_dictionary.dict")
tfidf.save("gensim_tfidf.model")
index.save("gensim_index.index")
