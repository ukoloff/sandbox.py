#
# Use Chroma for RAG
#
from pathlib import Path
from langchain_chroma import Chroma
from dotenv import load_dotenv
from gigachat import GigaChat
from langchain_gigachat import GigaChatEmbeddings

question = "Какой плащ был у Понтия Пилата?"

load_dotenv()

llm = GigaChat()
emb = GigaChatEmbeddings()

db = Chroma("m-m.giga", emb, persist_directory=str(Path(__file__).parent / ".db"))

retriever = db.as_retriever()
print(retriever.invoke(question))
