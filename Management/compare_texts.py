from langchain.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from Management.retrieve_Vectorizer import obtenir_fonction_embedding_travail

CHEMIN_CHROMA = ".\chroma"

# Configurer Template Prompt
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "Vous êtes AskLaw, un conseiller expert en droit du travail marocain. Utilisez le Code du travail marocain pour fournir des conseils précis et citez les numéros d'articles pertinents. Si la question n'est pas liée au droit du travail, indiquez que vous ne pouvez répondre qu'aux questions concernant le droit du travail marocain."),
        ("human", "Répondez en utilisant les informations suivantes : {context}"),
        ("human", "Voici ma question : {question}"),
    ]
)

def chercher_similarite_travail(question):
    # Préparation de la base de données.
    print("\n--- Initialisation de la base de données pour le droit du travail ---\n")
    fonction_embedding = obtenir_fonction_embedding_travail()
    db = Chroma(persist_directory=CHEMIN_CHROMA, embedding_function=fonction_embedding)
    print("\n--- La base de données a été initialisée avec succès ---\n")

    # Recherche dans la base de données.
    print("\n--- Recherche des informations pertinentes dans la base de données Chroma ---\n")
    results = db.similarity_search_with_score(question, k=5)
    if len(results) == 0:
        print("\n--- Aucune information trouvée pour votre question. Veuillez réessayer avec une autre question. ---\n")
    else:
        print("\n--- Recherche terminée. Voici les résultats pertinents : ---\n")

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt = prompt_template.format(context=context_text, question=question)
    print(prompt)
    return prompt
