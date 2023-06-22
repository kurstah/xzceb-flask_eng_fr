import unittest
from translator import englishToFrench, frenchToEnglish
class teste2f(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(englishToFrench('Hello'), 'Bonjour')

class testf2e(unittest.TestCase):
    def test2(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

unittest.main()