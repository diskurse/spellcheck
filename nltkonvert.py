# Script:  nltkonvert.py
# Desc:    A python 3 spell checking and algorithm testing module.
#
# Author:  Cian Heasley
# Created: 08/03/18
#  
"""
nltkonvert.py is a very simple Python script to take an input file and use
NLTK to strip extraneous punctuation and output a file that is all lower case
with one word per line.

This file is to be used as the input for other scripts that will implement
spell checking.
"""

import nltk
from nltk.corpus import stopwords
import string
import pprint

with open('ArthurConanDoyle.txt', 'r') as f:
    acd_raw = f.read()
    stop = set(stopwords.words('english'))
    acd_tokens = nltk.word_tokenize(acd_raw)
    text_no_stop_words_punct = [t for t in acd_tokens if t not in stop and t not in string.punctuation]
    cleanwords = [word.lower() for word in text_no_stop_words_punct]
    with open('acdoutput2.txt', 'w') as file_handler:
        for item in cleanwords:
            file_handler.write("{}\n".format(item))

