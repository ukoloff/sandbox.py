#
# Fetch DB
#
from pathlib import Path
from langchain_chroma import Chroma
from dotenv import load_dotenv
from langchain_gigachat import GigaChatEmbeddings

load_dotenv()

emb = GigaChatEmbeddings()

dbg = Chroma("m-m.giga", emb, persist_directory=str(Path(__file__).parent / ".db"))

question = "Какой плащ был у Понтия Пилата?"
docs = dbg.similarity_search(question)
print(docs)
