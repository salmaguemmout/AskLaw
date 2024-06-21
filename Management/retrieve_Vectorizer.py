from langchain.embeddings import OllamaEmbeddings

def obtenir_fonction_embedding_travail():
    """Fonction pour obtenir les embeddings spécifiques au droit du travail."""
    return OllamaEmbeddings(model="nomic-embed-text")
