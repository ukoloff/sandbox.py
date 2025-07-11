#
# Embedding function adapter
#
import numpy as np
from gigachat import GigaChat
from chromadb import Documents, EmbeddingFunction, Embeddings


class GigaChatEmb(EmbeddingFunction):
    def __init__(self, model_name="Embeddings"):
        super().__init__()
        self.llm = GigaChat() #verify_ssl_certs=False)
        if model_name == "+":
            model_name = "EmbeddingsGigaR"
        self.model = model_name

    def __call__(self, input: Documents) -> Embeddings:
        res = self.llm.embeddings(input, model=self.model)
        return [np.array(emb.embedding) for emb in res.data]

if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()

    emb = GigaChatEmb()
    print(emb(['Hello']))
