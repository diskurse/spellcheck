# Script:  nltkonvert.py
# Desc:    A python 3 spell checking and algorithm testing module.
#
# Author:  Cian Heasley
# Created: 08/03/18
#  
"""
Scraper.py is a Python web page scraping/information gathering reconnaissance 
utility. This program retrieves web content and parses this for specified 
information, and then performs some forensic analysis on the contents.
The application will read the webpage source code from a specified URL and 
analyse the webpage by parsing out links to information such as subpages and files,
as well as parsing out any interesting artefacts such as email addresses and 
possible hashed passwords. 

Example:

        $ python scraper.py --url [URL to scrape]


Todo:
    * Added parsing functionality
    * Better error handling
    * More argparse functionality

Code taken and modified from stackoverflow, Violent Python, Python for Beginners and BeautifulSoup
documentation.
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

