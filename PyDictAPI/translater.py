"""
Author: Shawan Mandal
    
MIT License, see LICENSE for more details.
Copyright (c) 2021 Shawan Mandal

"""

import urllib.request
import urllib.parse, sys, goslate

try:
    from utils import getSoupObj
except:
    from .utils import getSoupObj

class PythonVersionError(Exception):
    pass

class Translate(object):

    def __init__(self):
        self.searching = "Please wait while I translate your query"
        self.CONTENT_HEADERS = {'User-Agent': 
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
        self.isPython3 = True
        
        if (sys.version_info.major) < 3:
            self.isPython3 = False
        else:
            pass

    def translateItems(self, query, translateLang="auto", from_lang="auto"):
        """Trabslates a word or sentence using google translate and returns the translated result in an python list
        """

        if (self.isPython3):
            pass
        else:
            raise PythonVersionError("Python version 3 or newer is required")

        query = urllib.parse.quote(query)
        URL = f"http://translate.google.com/m?tl={translateLang}&sl={from_lang}&q={query}"

        request = urllib.request.Request(URL, headers=self.CONTENT_HEADERS)
        responseData = urllib.request.urlopen(request).read()
        data = getSoupObj(responseData)
        translatedItems = []
        try:
            for each in data.findAll(attrs={"class": "result-container"}):
                translatedItems.append(each.text)
        except:
            return "Couldn't translate your query, please try searching the web..."

        return translatedItems
