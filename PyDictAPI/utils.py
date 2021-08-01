"""
Author: Shawan Mandal
    
MIT License, see LICENSE for more details.
Copyright (c) 2021 Shawan Mandal

"""

import requests
from bs4 import BeautifulSoup

def handleRequests(query):
    '''Returns HTML document'''
    try:
        response = requests.get(f'https://www.dictionary.com/browse/{query}').text
        return response
    except Exception:
        raise ConnectionError("Error occured while fetching data from the web, please try checking the internet connection.")

def ParseUsagePage(query):
    '''Returns HTML document'''
    try:
        response = requests.get(f'https://www.lexico.com/en/definition/{query}').text
        return response
    except Exception:
        raise ConnectionError("Error occured while fetching data from the web, please try checking the internet connection.")

def getSoupObj(res):
    '''Returns BeautifulSoup Object'''
    return BeautifulSoup(res, "html.parser")

