from dotenv import load_dotenv
from gigachat import GigaChat

load_dotenv()

llm = GigaChat(verify_ssl_certs=False)


q = llm.chat('Однажды в студёную зимнюю пору?')
print(q.choices[0].message.content)
