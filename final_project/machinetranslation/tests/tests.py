import unittest
from translator import english_to_french, french_to_english
class teste2f(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(english_to_french('Hello'), 'Bonjour')

class testf2e(unittest.TestCase):
    def test2(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()