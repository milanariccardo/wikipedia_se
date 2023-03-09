# -*- coding: utf-8 -*-
"""
@author: franc, Ricc
"""

import xml.sax
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
import string

import whoosh
from whoosh.index import create_in
from whoosh.fields import *
import os, os.path

''' Definizione dello schema '''
schema = Schema(title=TEXT(stored=True),content=TEXT)
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")
ix = create_in("indexdir", schema)


class WikiHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.title = ""
        self.text = []
        self.lista = []
        self.flag = False

    def startElement(self, tag, attr):
        self.CurrentData = tag

    def characters(self, content):
        if self.CurrentData == "title":
            self.title = self.title+content
        elif self.CurrentData == "text":
            if self.flag == False:
                #self.flag = remove_from_references(content)
	    	#self.lista = remove_references_link(content, self.lista)
                if len(self.lista) <=3:
                    self.text.append(content)
                    #print(content)

    def endElement(self, tag):
        if self.CurrentData == "title":
            print("Title: ",self.title)
        elif self.CurrentData == "text":
            writer = ix.writer()
            writer.add_document(title = remove_special_character(self.title), content = processText(self.text))
            writer.commit()
            self.title = ""
            self.text.clear()
            self.flag = False
            self.lista.clear()

def remove_special_character(text):
    testo = re.sub(r'[^A-Za-z0-9]+', r' ', str(text))
    return testo

def processText(text):
    testo = remove_special_character(text)
    tokens = nltk.word_tokenize(str(testo))
    lista = []
    for t in tokens:
        if not t in stopwords.words('english') and t not in string.punctuation and t != 'n':
            lista.append(t)
    lista_stem = []
    for t in lista:
        #lista_stem.append(lemmatizer.lemmatize(t))
        #lista_stem.append(porter.stem(t))
        lista_stem.append(t)
    return lista_stem


''' Rimuovi i link all'interno del testo '''

def remove_references_link(text, lista):
    if len(lista) == 6:
        lista.clear()

    if re.match(r'^<$',text):
        lista.clear()
        lista.append(text)
        return lista

    if re.match(r'^ref.*$',text):
        if len(lista) == 1:
            lista.append(text)
        else:
            lista.clear()
        return lista

    if re.match(r'^>$',text):
        if len(lista) == 2:
            lista.append(text)
        else:
            lista.clear()
        return lista

    #Se incontro la sequenza "< ref.* >" aggingo il link alla lista[4] oppure "< ref.* > link & "
    if (len(lista) == 3) or (len(lista) == 5):
        lista.append(text)
        return lista

    #Se incontro la sequenza "< ref.* > link" aggingo & alla lista[5]
    if len(lista) == 4:
        if re.match(r'^&$',text):
            lista.append(text)
            return lista
        else:
            lista.clear()
    return lista


def remove_from_references(text):
    if re.match(r'^== (R|r)eferences ==$',text):
        return True
    return False


if ( __name__ == "__main__"):

   # create an XMLReader
   parser = xml.sax.make_parser()
   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # override the default ContextHandler
   Handler = WikiHandler()
   parser.setContentHandler( Handler )
   parser.parse(sys.argv[1])
