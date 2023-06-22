"""
This module contains functions to translate text between English and French.
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translate text from English to French using MyMemoryTranslator.
    """
    translator = MyMemoryTranslator(source='en', target='fr')
    french_text = translator.translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    Translate text from French to English using MyMemoryTranslator.
    """
    translator = MyMemoryTranslator(source='fr', target='en')
    english_text = translator.translate(french_text)
    return english_text
    