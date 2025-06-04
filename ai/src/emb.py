#
# Free embeddings
#
from langchain.embeddings import HuggingFaceEmbeddings

emb = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')

res = emb.embed_query("Однажды в студёную зимнюю пору")
print(res)
