import unittest
import os
import shutil
import sys

# Add the project root directory to the PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from Management.reset_data import effacer_base_donnees_travail, CHEMIN_CHROMA

class TestResetData(unittest.TestCase):
    
    def setUp(self):
        os.makedirs(CHEMIN_CHROMA, exist_ok=True)
    
    def tearDown(self):
        if os.path.exists(CHEMIN_CHROMA):
            shutil.rmtree(CHEMIN_CHROMA)
    
    def test_effacer_base_donnees_travail(self):
        effacer_base_donnees_travail()
        self.assertFalse(os.path.exists(CHEMIN_CHROMA), "Database directory should be deleted.")

if __name__ == '__main__':
    unittest.main()
