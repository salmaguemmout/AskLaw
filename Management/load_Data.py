import logging
import time
from langchain_community.document_loaders.pdf import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from Management.retrieve_Vectorizer import obtenir_fonction_embedding_travail
from langchain_community.vectorstores import Chroma

CHEMIN_CHROMA = "./chroma"
CHEMIN_DONNEES = "./Data"

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def processus_principal_embeddings():
    logging.debug("Starting processus_principal_embeddings")
    try:
        tic = time.time()
        
        # Load documents
        documents = charger_documents_travail()
        if not documents:
            logging.error("No documents loaded")
            return None
        logging.debug(f"Loaded {len(documents)} documents")
        
        # Divide documents into chunks
        morceaux = diviser_documents_travail(documents)
        if not morceaux:
            logging.error("Documents not divided into chunks")
            return None
        logging.debug(f"Divided into {len(morceaux)} chunks")
        
        # Add document chunks to Chroma database
        ajouter_documents_travail_a_chroma(morceaux)
        
        toc = time.time()
        logging.debug(f"Processus terminé en : {(toc - tic)} secondes")
        return True
    except Exception as e:
        logging.exception("Exception occurred in processus_principal_embeddings")
        return None

def charger_documents_travail():
    logging.debug("Loading documents")
    try:
        chargeur_documents = PyPDFDirectoryLoader(CHEMIN_DONNEES)
        documents = chargeur_documents.load()
        logging.debug(f"Loaded documents: {documents}")
        return documents
    except Exception as e:
        logging.exception("Exception occurred in charger_documents_travail")
        return None

def diviser_documents_travail(documents: list[Document]):
    logging.debug("Dividing documents into chunks")
    try:
        diviseur_textes = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=80,
            length_function=len,
            is_separator_regex=False,
        )
        morceaux = diviseur_textes.split_documents(documents)
        logging.debug(f"Divided documents: {morceaux}")
        return morceaux
    except Exception as e:
        logging.exception("Exception occurred in diviser_documents_travail")
        return None

def ajouter_documents_travail_a_chroma(morceaux: list[Document]):
    logging.debug("Adding documents to Chroma")
    try:
        db = Chroma(
            persist_directory=CHEMIN_CHROMA, embedding_function=obtenir_fonction_embedding_travail()
        )
        morceaux_avec_ids = calculer_ids_morceaux_travail(morceaux)
        elements_existants = db.get(include=[])
        ids_existants = set(elements_existants["ids"])
        logging.debug(f"Existing document IDs in database: {ids_existants}")
        nouveaux_morceaux = [morceau for morceau in morceaux_avec_ids if morceau.metadata["id"] not in ids_existants]
        
        if nouveaux_morceaux:
            logging.debug(f"Adding new documents: {len(nouveaux_morceaux)}")
            ids_nouveaux_morceaux = [morceau.metadata["id"] for morceau in nouveaux_morceaux]
            db.add_documents(nouveaux_morceaux, ids=ids_nouveaux_morceaux)
            db.persist()
        else:
            logging.debug("No new documents to add")
    except Exception as e:
        logging.exception("Exception occurred in ajouter_documents_travail_a_chroma")

def calculer_ids_morceaux_travail(morceaux):
    logging.debug("Calculating IDs for document chunks")
    try:
        dernier_id_page = None
        index_morceau_courant = 0

        for morceau in morceaux:
            source = morceau.metadata.get("source")
            page = morceau.metadata.get("page")
            id_page_courant = f"{source}:{page}"

            if id_page_courant == dernier_id_page:
                index_morceau_courant += 1
            else:
                index_morceau_courant = 0

            id_morceau = f"{id_page_courant}:{index_morceau_courant}"
            dernier_id_page = id_page_courant
            morceau.metadata["id"] = id_morceau

        logging.debug(f"Document chunks with IDs: {morceaux}")
        return morceaux
    except Exception as e:
        logging.exception("Exception occurred in calculer_ids_morceaux_travail")
        return None
