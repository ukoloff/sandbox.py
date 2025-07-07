from fastembed import TextEmbedding

supported_models = TextEmbedding.list_supported_models()
for m in supported_models:
    print(m['model'], m['dim'], m['size_in_GB'], m['description'], sep="\t")
