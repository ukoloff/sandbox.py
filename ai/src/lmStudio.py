from openai import OpenAI
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    openai_api_base='http://127.0.0.1:1234/v1',
    api_key="none"
)

print(llm.invoke('Привет!'))

ai = OpenAI(base_url='http://127.0.0.1:1234/v1', api_key='none')
res = ai.chat.completions.create(messages=[{"role": "user", "content": 'Как дела на плюке'}], model='saiga_mistral_7b_gguf')
print(res)

emb = ai.embeddings.create(input=['Плащ Понтия Пилата'], model='text-embedding-nomic-embed-text-v1.5')
print(emb)
