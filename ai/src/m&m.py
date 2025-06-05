#
# Import large text
#
from pathlib import Path
from typing import List
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from chromadb.utils import embedding_functions

src = Path(__file__).parents[1] / 'data' / 'мастер_и_маргарита.txt'
doc = TextLoader(src).load()
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)
docs = text_splitter.split_documents(doc)
print(f"documents: {len(docs)}")

# emb = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
# ^ Chroma does it itself
# https://docs.trychroma.com/docs/embeddings/embedding-functions
ef = embedding_functions.DefaultEmbeddingFunction()

class DefEmb:
    def embed_query(self, text: str) -> List[float]:
        return ef([text])[0]

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return ef(texts)

db = Chroma.from_documents(docs, DefEmb())

question = "Какой плащ был у Понтия Пилата?"
docs = db.similarity_search(question)
print(docs)
