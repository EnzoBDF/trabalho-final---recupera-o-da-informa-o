from whoosh.index import create_in
from whoosh.fields import Schema, TEXT
import os

schema = Schema(title=TEXT(stored=True), content=TEXT)
os.makedirs("whoosh_index", exist_ok=True)
ix = create_in("whoosh_index", schema)

writer = ix.writer()
writer.add_document(title="Doc1", content="Os gatos domésticos são amigáveis e carinhosos.")
writer.add_document(title="Doc2", content="Felinos selvagens vivem em florestas e são caçadores.")
writer.add_document(title="Doc3", content="Os cães também são animais domésticos muito leais.")
writer.commit()