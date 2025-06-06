#
# Use Chroma for RAG
#
from pathlib import Path
from langchain_chroma import Chroma
from dotenv import load_dotenv
from langchain_gigachat.chat_models import GigaChat
from langchain_gigachat import GigaChatEmbeddings
from langchain_core.runnables import RunnablePassthrough
from langchain import hub
from langchain_core.output_parsers import StrOutputParser

question = "Какой плащ был у Понтия Пилата?"

load_dotenv()

llm = GigaChat()
emb = GigaChatEmbeddings()

db = Chroma("m-m.giga", emb, persist_directory=str(Path(__file__).parent / ".db"))


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


prompt = hub.pull("rlm/rag-prompt")

retriever = db.as_retriever()

chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough(),
    }
    | prompt
    | llm
    | StrOutputParser()
)


res = chain.invoke(question)
print(res)
