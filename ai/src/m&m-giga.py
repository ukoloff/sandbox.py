#
# Import large text
#
from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
from langchain_gigachat import GigaChatEmbeddings


src = Path(__file__).parents[1] / "data" / "мастер_и_маргарита.txt"
doc = TextLoader(src).load()
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)
docs = text_splitter.split_documents(doc)
print(f"documents: {len(docs)}")

# https://github.com/ai-forever/gigachat

load_dotenv()

emb = GigaChatEmbeddings()

db = Chroma.from_documents(
    docs,
    emb,
    persist_directory=str(Path(__file__).parent / ".db"),
    collection_name="m-m.giga",
)

question = "Какой плащ был у Понтия Пилата?"
docs = db.similarity_search(question)
print(docs)
