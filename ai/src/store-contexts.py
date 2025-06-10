#
# Use Chroma for RAG
#
import yaml
from pathlib import Path
from langchain_chroma import Chroma
from dotenv import load_dotenv
from langchain_gigachat import GigaChatEmbeddings
from langchain_core.runnables import RunnablePassthrough

questions = [
    "Какой плащ был у Понтия Пилата?",
    "Какая трость была у Воланда?",
    "В чем главная проблема человека?",
]

load_dotenv()

emb = GigaChatEmbeddings()

db = Chroma("m-m.giga", emb, persist_directory=str(Path(__file__).parent / ".db"))

contexts = dict(
    (q, [doc.page_content for doc in db.similarity_search(q)]) for q in questions
)

dst = Path(__file__).parents[1] / "data" / "contexts.yml"

yaml.dump(contexts, dst.open("w", encoding="utf-8"), allow_unicode=True)
