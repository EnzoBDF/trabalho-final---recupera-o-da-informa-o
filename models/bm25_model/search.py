from rank_bm25 import BM25Okapi
import json
import os

# Documentos de entrada
documents = [
    "Os gatos domésticos são amigáveis e carinhosos.",
    "Felinos selvagens vivem em florestas e são caçadores.",
    "Os cães também são animais domésticos muito leais."
]
doc_ids = ["Doc1", "Doc2", "Doc3"]

# Tokenização simples
tokenized_docs = [doc.lower().split() for doc in documents]

# Criar BM25
bm25 = BM25Okapi(tokenized_docs)

# Consulta
query = "gatos domésticos".lower().split()
scores = bm25.get_scores(query)

# Ordenar resultados
ranking = sorted(zip(doc_ids, scores), key=lambda x: x[1], reverse=True)

# Mostrar e salvar resultados
print(\"\\nResultados BM25:\")
results = []
for doc_id, score in ranking:
    print(f\"{doc_id}: Score = {score:.4f}\")
    results.append(doc_id)

# Salvar no formato JSON para usar nas métricas
os.makedirs(\"../../results\", exist_ok=True)
with open(\"../../results/bm25_results.json\", \"w\") as f:
    json.dump(results, f, indent=2)
