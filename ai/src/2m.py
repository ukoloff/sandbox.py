#
# Use Chroma for RAG
#
from dotenv import load_dotenv
from gigachat import GigaChat as GiChat
from langchain_gigachat.chat_models import GigaChat

question = "Какой плащ был у Понтия Пилата?"

load_dotenv()

llmG = GiChat()
llmL = GigaChat()

resG = llmG.chat(question)
resL = llmL.invoke(question)

print(resG)
print(resL)
