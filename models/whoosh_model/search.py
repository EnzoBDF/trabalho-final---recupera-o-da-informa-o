from whoosh.index import open_dir
from whoosh.qparser import QueryParser

ix = open_dir("whoosh_index")
with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema).parse("gatos AND domésticos")
    results = searcher.search(query)
    for hit in results:
        print(hit["title"])