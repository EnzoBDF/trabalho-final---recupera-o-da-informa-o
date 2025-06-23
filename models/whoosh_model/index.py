from whoosh.index import create_in
from whoosh.fields import Schema, TEXT
import os

DIR = os.path.dirname(os.path.abspath(__file__))
PATH_DOCS = os.path.join(DIR, '..', '..', 'data', 'documents.txt')

def ler_documentos(path):
    docs = []
    with open(path, encoding='utf-8') as f:
        for linha in f:
            if linha.strip():
                doc_id, conteudo = linha.strip().split('\t', 1)
                docs.append((doc_id, conteudo))
    return docs

schema = Schema(title=TEXT(stored=True), content=TEXT)
os.makedirs("whoosh_index", exist_ok=True)
ix = create_in("whoosh_index", schema)

writer = ix.writer()
for doc_id, conteudo in ler_documentos(PATH_DOCS):
    writer.add_document(title=doc_id, content=conteudo)
writer.commit()