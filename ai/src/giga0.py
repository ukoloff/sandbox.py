from dotenv import load_dotenv
from gigachat import GigaChat
# https://github.com/ai-forever/gigachat

load_dotenv()

llm = GigaChat(verify_ssl_certs=False)

# Query
q = llm.chat("Однажды в студёную зимнюю пору?")
print(q.choices[0].message.content)

# Embedding
emb = llm.embeddings(["Однажды в студёную зимнюю пору?"])
print(emb)
