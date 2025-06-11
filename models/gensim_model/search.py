from gensim import corpora, models, similarities

query = "gatos domésticos"
dictionary = corpora.Dictionary.load("gensim_dictionary.dict")
tfidf = models.TfidfModel.load("gensim_tfidf.model")
index = similarities.MatrixSimilarity.load("gensim_index.index")

query_bow = dictionary.doc2bow(query.lower().split())
sims = index[tfidf[query_bow]]

for i, score in enumerate(sims):
    print(f"Doc{i+1}: Similaridade = {score:.4f}")