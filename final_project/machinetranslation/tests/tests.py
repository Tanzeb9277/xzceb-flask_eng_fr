from translator import english_to_french, french_to_english
import unittest
import json

class TestFrenchTranslation(unittest.TestCase):
    def test1(self):
        self.assertIsNotNone(english_to_french('Hello'))
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestEnglsihTranslation(unittest.TestCase):
    def test1(self):
        self.assertIsNotNone(english_to_french('Bonjour'))
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()
