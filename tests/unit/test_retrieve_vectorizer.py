import unittest
import os
import sys

# Add the project root directory to the PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from Management.retrieve_Vectorizer import obtenir_fonction_embedding_travail
from langchain.embeddings import OllamaEmbeddings

class TestRetrieveVectorizer(unittest.TestCase):
    
    def test_obtenir_fonction_embedding_travail(self):
        embedding_function = obtenir_fonction_embedding_travail()
        self.assertIsInstance(embedding_function, OllamaEmbeddings, "The embedding function should be an instance of OllamaEmbeddings.")

if __name__ == '__main__':
    unittest.main()
