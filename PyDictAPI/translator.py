"""
Author: Shawan Mandal
    
MIT License, see LICENSE for more details.
Copyright (c) 2021 Shawan Mandal

"""

import urllib.request
import urllib.parse, sys, json, requests
from urllib.parse import urlencode

try:
    from utils import getSoupObj, handleRequests
except:
    from .utils import getSoupObj, handleRequests

class PythonVersionError(Exception):
    pass

class Translate(object):
    """
    ## PyDictAPI: Translator - The Free Translation API
    
    You have to first create an instance of Translate to use this API

    ### Example:
    >>> # Import the module first
    >>> from PyDictAPI import Translate
    >>> t = Translate(jsonify=True) #   Creates an instance of Translate class
    >>> # jsonify=True returns response in JSON, and by default jsonify is False
    >>> # You can get all supported language list through languages_help()
    >>> languages = t.languages_help())
    >>> 
    >>> # Tranlate English into Hindi
    >>> print(t.translateItems("Hello, How are you?", "hi"))

    `{'query': 'Hello, How are you?', 'language_detected': 'Hindi', 'translation': 'नमस्कार किसे हो आप?'}`
    """
    def __init__(self, jsonify=False):
        self.__jsonify = jsonify
        self.__searching = "Please wait while I process your query... \n"
        self.__CONTENT_HEADERS = {'User-Agent': 
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
        self.isPython3 = True
        self.__SUPPORTED_LANGUAGES = {}
        self.__prettyText = "List of the Languages Supported... \n\n"
        
        if (sys.version_info.major) < 3:
            self.isPython3 = False
        else:
            pass
    
    def __prettyPrint(self):
        """
        ### Pretty prints text
        """
        SUPPORTED_LANGUAGES = json.loads(self.__SUPPORTED_LANGUAGES)
        data = SUPPORTED_LANGUAGES['sl']
        prettyText = self.__prettyText
        for key in data.keys():
            prettyText += key + ": \t" + data[key] + "\n"
        return prettyText

    def languages_help(self):
        '''
        # Returns supported languages

        It returns language codes for supported languages for translation. 
        Some language codes also include a country code, like zh-CN or zh-TW.

        :Example:

        >>> from PyDictAPI import Translate
        >>> t = Translate(jsonify=True)
        >>> print(t.languages_help())

        jsonify=True returns a json response,
        and by default jsonify is False

        '''

        if (self.isPython3):
            pass
        else:
            raise PythonVersionError("Python version 3 or newer is required")
        print(self.__searching)    
        if self.__SUPPORTED_LANGUAGES and self.__jsonify == False:
            return self.__SUPPORTED_LANGUAGES
        
        TRASLATOR_URL = 'http://translate.google.com/translate_a/l'
        TRASLATOR_PARAMS = {
            'client': 't',
            }
        url = '?'.join((TRASLATOR_URL, urlencode(TRASLATOR_PARAMS)))
        response_content = requests.get(url, headers=self.__CONTENT_HEADERS).text
        self.__SUPPORTED_LANGUAGES = json.loads(response_content)
        self.__SUPPORTED_LANGUAGES = json.dumps(self.__SUPPORTED_LANGUAGES, indent=2)
        if not self.__jsonify:
            return self.__prettyPrint()

        return self.__SUPPORTED_LANGUAGES

    def translateItems(self, query, translateLang="auto", from_lang="auto"):
        """
        Translates a word or sentence using google translate and returns the translated result.

        ### Example:
        >>> # Import the module first
        >>> from PyDictAPI import Translate
        >>> t = Translate(jsonify=true) #   Creates an instance of Translate class
        >>> 
        >>> # Tranlate English into Hindi
        >>> print(t.translateItems("Hello, How are you?", "hi"))

        `{'query': 'Hello, How are you?', 'language_detected': 'Hindi', 'translation': 'नमस्कार किसे हो आप?'}`
        """

        if (self.isPython3):
            pass
        else:
            raise PythonVersionError("Python version 3 or newer is required")
        text = query
        print(self.__searching)    

        query = urllib.parse.quote(query)
        URL = f"http://translate.google.com/m?tl={translateLang}&sl={from_lang}&q={query}"

        request = urllib.request.Request(URL, headers=self.__CONTENT_HEADERS)
        responseData = urllib.request.urlopen(request).read()
        data = getSoupObj(responseData)
        translatedList = []
        processedItem = ""
        Translation = {}
        try:
            lang = data.find(attrs={"class": "languages-container"}).find_all("a")
            lang = lang[1].text
        except:
            lang = "null"

        try:
            temp = data.findAll(attrs={"class": "result-container"})
            if len(temp) > 1:
                for each in temp:
                    translatedList.append(each.text)
                Translation = {
                "query": text,
                "language": lang,
                "translation": translatedList
                }
                processedItem = translatedList

            else:
                Translation = {
                "query": text,
                "language": lang,
                "translation": temp[0].text
                }
                processedItem = temp[0].text
        except:
            Translation = {
                "query": text,
                "message": "Couldn't translate your query, please try searching the web..."
                }
        if self.__jsonify:
            return json.dumps(Translation, indent=2, ensure_ascii=False)
        else:
            return processedItem