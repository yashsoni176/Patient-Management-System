import unittest
import sqlite3

class Patient(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect("hospital.db")
        self.patientcode = "110"
        self.name = "Yash"
    def tearDown(self):
        self.patientcode = "0"
        self.name = ""
        self.connection.close()

    def test_case_patient(self):
        result = self.connection.execute("Select name from patient where patientcode = "+self.patientcode)

        for i in result:
            namefetch = i[0]
        self.assertEqual(namefetch, self.name)

if __name__ == "__main__":
    unittest.main