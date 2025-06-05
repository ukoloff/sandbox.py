#
# Import large text
#
from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

src = Path(__file__).parents[1] / 'data' / 'мастер_и_маргарита.txt'
doc = TextLoader(src).load()
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)
docs = text_splitter.split_documents(doc)
print(f"documents: {len(docs)}")
