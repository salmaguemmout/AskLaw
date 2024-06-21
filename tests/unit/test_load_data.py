import unittest
import os
import sys
import shutil

# Add the project root directory to the PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from Management.load_Data import charger_documents_travail, diviser_documents_travail, calculer_ids_morceaux_travail, CHEMIN_DONNEES
from langchain.schema.document import Document

class TestLoadData(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Ensure the data directory exists
        if not os.path.exists(CHEMIN_DONNEES):
            os.makedirs(CHEMIN_DONNEES)
        # Create a dummy PDF file
        with open(os.path.join(CHEMIN_DONNEES, 'test.pdf'), 'w') as f:
            f.write("%PDF-1.4\n1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R >>\nendobj\n4 0 obj\n<< /Length 55 >>\nstream\nBT\n/F1 24 Tf\n100 700 Td\n(Test PDF) Tj\nET\nendstream\nendobj\nxref\n0 5\n0000000000 65535 f \n0000000010 00000 n \n0000000063 00000 n \n0000000110 00000 n \n0000000200 00000 n \ntrailer\n<< /Size 5 /Root 1 0 R >>\nstartxref\n261\n%%EOF")
    
    @classmethod
    def tearDownClass(cls):
        # Remove the data directory and its contents after tests
        if os.path.exists(CHEMIN_DONNEES):
            shutil.rmtree(CHEMIN_DONNEES)
    
    def test_charger_documents_travail(self):
        documents = charger_documents_travail()
        self.assertTrue(len(documents) > 0, "No documents loaded.")
    
    def test_diviser_documents_travail(self):
        documents = [Document(page_content="Test document content", metadata={"source": "test", "page": 1})]
        morceaux = diviser_documents_travail(documents)
        self.assertTrue(morceaux, "Documents should be divided into chunks.")
    
    def test_calculer_ids_morceaux_travail(self):
        documents = [Document(page_content="Test document content", metadata={"source": "test", "page": 1})]
        morceaux = calculer_ids_morceaux_travail(documents)
        self.assertTrue(morceaux[0].metadata["id"], "Chunks should have calculated IDs.")

if __name__ == '__main__':
    unittest.main()
