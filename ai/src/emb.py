#
# Free embeddings
#
from langchain_huggingface import HuggingFaceEmbeddings

emb = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')

res = emb.embed_query("Однажды в студёную зимнюю пору")
print(res)
print(len(res))
