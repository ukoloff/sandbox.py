#
# Fetch DB
#
from typing import List
from pathlib import Path
from langchain_community.vectorstores import Chroma
from chromadb.utils import embedding_functions

# https://docs.trychroma.com/docs/embeddings/embedding-functions
ef = embedding_functions.DefaultEmbeddingFunction()


class DefEmb:
    def embed_query(self, text: str) -> List[float]:
        return ef([text])[0]

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return ef(texts)


db = Chroma("m-m.def", DefEmb(), persist_directory=str(Path(__file__).parent / ".db"))

question = "Какой плащ был у Понтия Пилата?"
docs = db.similarity_search(question)
print(docs)
