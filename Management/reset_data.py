import argparse
import os
import shutil
from langchain.document_loaders.pdf import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from Management.retrieve_Vectorizer import obtenir_fonction_embedding_travail
from langchain_community.vectorstores import Chroma
import time

CHEMIN_CHROMA = "./chroma"
CHEMIN_DONNEES = "./Data"

def effacer_base_donnees_travail():
    if os.path.exists(CHEMIN_CHROMA):
        shutil.rmtree(CHEMIN_CHROMA)
        print("La base de données Chroma a été supprimée avec succès.")
    else:
        print("Aucune base de données Chroma à supprimer.")

if __name__ == "__main__":
    effacer_base_donnees_travail()
