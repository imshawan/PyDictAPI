[![PyDictAPI](https://img.shields.io/badge/PyDictAPI-Stable-limegreen)](https://github.com/imshawan/PyDictAPI)
[![GitHub license](https://img.shields.io/github/license/imshawan/PyDictAPI)](https://github.com/imshawan/PyDictAPI/blob/master/LICENSE.txt)
[![Latest Version](http://img.shields.io/pypi/v/PyDictAPI.svg?style=flat-square)](https://pypi.python.org/pypi/PyDictAPI/)
[![Downloads](https://img.shields.io/pypi/dm/PyDictAPI.svg?style=flat-square)](https://pypi.python.org/pypi/PyDictAPI/)

# PyDictAPI
### An advanced Dictionary and Translator Module for Python

PyDictAPI is a Dictionary Module for Python 3+ to get a detailed and well-structured meanings of a queried word in JSON format. PyDictAPI searches for the query on the web, if the query matches than it returns the Definitions/Examples/Synonyms/Antonyms as specified by the user. And incase of incorrect words, the response is returned as a suggestion of the correct word.<br>
And incase of wrong translation-query or language code, the source query is returned back.

>  **Sources:** [Dictionary.com](https://www.dictionary.com/), [Thesaurus](https://www.thesaurus.com/), [Lexico](https://www.lexico.com/)

This module uses Requests and bs4 dependencies to scrape the web and find the definitions and return it in a well-structured JSON document

## Installation

PyDictAPI can be easily installed through [PIP](https://pip.pypa.io/en/stable/)

```
pip install PyDictAPI
```
### [View Changelog](https://github.com/imshawan/PyDictAPI/blob/master/CHANGELOG.md)

###  Both the Finder and Translator class takes an arguement "jsonify" that is set to False by default. If jsonify is set to True, than the processed queries are returned in JSON. While by default the queries are returned in the form of a Python List (Array)

## Dictionary searches

Dictionary searches can be performed by creating a Finder instance and later calling findMeanings() that takes a word as an arguement.

For example,

```python
from PyDictAPI import Finder
Meanings = Finder(jsonify=True)
# Use can use Finder() without 'jsonify' to get response in the form of a Python List
print(Meanings.findMeanings('apple'))
```

This is will create a local instance of the Finder class and will return results containing the meanings of the word. <br>
The Output can be seen as:

```
{
  "word": "Apple",
  "meanings": [
    {
      "partOfSpeech": "Noun",
      "definition": "The usually round, red or yellow, edible fruit of a small tree, Malus sylvestris, of the rose family."  
    },
    {
      "partOfSpeech": "Noun",
      "definition": "A rosaceous tree, Malus sieversii, native to Central Asia but widely cultivated in temperate regions in many varieties, having pink or white fragrant flowers and firm rounded edible fruits. See also crab apple"
    }
  ]
}                                                                       
```
## Exceptions

### Case - 1: If the word is spelt incorrectly

```python
from PyDictAPI import Finder
Meanings = Finder()
# jsonify is set to false by default, so the output returned is in plain string.
print(Meanings.findMeanings('helloooo'))
```
Incase of incorrect words, the response is returned as a suggestion of the correct word <br>
The Response can be seen as:

```
Couldn't find results for helloooo, Did you mean hello?
```

### Case - 2: If the word doesn't exist

```python
from PyDictAPI import Finder
Meanings = Finder()
print(Meanings.findMeanings('abcdefghijkl'))
```
The Response can be seen as:

```
Couldn't find any results for ABCDEFGHIJKL, try searching the web...
```
## Finding Examples, Synonyms and Antonyms

```python
from PyDictAPI import Finder
Meanings = Finder()
# jsonify is set to false by default, so the output returned is in python list.

print(Meanings.findUsage('help', 2)) #Finding Examples
# Here 2 defines the maximum number of examples to be included in the response, 
# by default it is set to 5

print(Meanings.findSynonyms('help', 4)) #Finding Synonyms
print(Meanings.findAntonyms('help', 4)) #Finding Antonyms

```

### Outputs for Examples, Synonyms and Antonyms

Examples: <br>
```
['She helped him find a buyer', 'Long-term funding is desperately being sought for a voluntary service that helps local victims of domestic violence.']
```

Synonyms: <br>
```
['Advice', 'Aid', 'Benefit', 'Comfort']
```

Antonyms: <br>
```
['Blockage', 'Encumbrance', 'Handicap', 'Hindrance']
```

## Using the Translator

```python
from PyDictAPI import Translate
t = Translate(jsonify=True)
print(t.languages_help()) # Prints all supported languages with language code

print(t.translateItems("Hello, How are you?", "hi")) # hi: Hindi

# Translates text according to the language code
```
Output:
```
{'query': 'Hello, How are you?', 'language': 'Hindi', 'translation': 'नमस्कार किसे हो आप?'}
```

## About

Copyright (c) 2021 Shawan Mandal.
