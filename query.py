# -*- coding: utf-8 -*-
"""
@author: franc, Ricc
"""
from whoosh import qparser
from whoosh import scoring
from whoosh import scoring

from whoosh.index import open_dir
from whoosh.qparser import QueryParser
import re
import tkinter as tk
import tkinter.scrolledtext as tkst
import os

import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
import string

#Funzione che definisce il comportamento dopo aver premuto il pulsante cerca
def azione(self):
   #Sblocco lo stato di scrolledtext
   self.Scrolledtext1.config(state= "normal")
   v=self.entry.get()
   if (v != ' '):
       query(v, self.Scrolledtext1)
   #Blocco lo stato di scrolledtext: in questo modo l'utente non può scrivere nello Scrolledtext
   self.Scrolledtext1.config(state= "disable")

#Funzione che definisce il comportamento dopo aver premuto il pulsante pulisci
def pulisci(self):
    self.Scrolledtext1.config(state= "normal")
    self.Scrolledtext1.delete('1.0', tk.END)
    self.entry.delete(0, tk.END)
    self.Scrolledtext1.config(state= "disable")


def preprocessing(text):
    tokens = nltk.word_tokenize(str(text))
    lista = []
    for t in tokens:
        if not t in stopwords.words('english') and t not in string.punctuation and t != 'n':
            lista.append(t)
    testo = ' '.join(lista)
    return testo

def remove_special_character(text):
    testo = re.sub(r'[^A-Za-z0-9]+', r' ', str(text))
    return testo

def pos_score_fn(searcher, fieldname, text, matcher):
    poses = matcher.value_as("positions")
    return 1.0 / (poses[0] + 1)




def query(text, finestra):
    searcher = ix.searcher(weighting = scoring.TF_IDF())

    ''' Processing della query '''
    testo = preprocessing(text)

    ''' Query expansion (con solo 3 sinonimi) '''

    synonyms = []
    count = 0
    for i in testo.split():
        synonyms.append(i)
        for syn in wordnet.synsets(i):
                for l in syn.lemmas() :
                    if(count<3):
                        if l.name() not in synonyms:
                            synonyms.append(l.name())
                            count+=1
        count = 0

    query_espansa = ' '.join(synonyms)

    #testo = remove_special_character(query_espansa)
    ''' Modifica del Query parser: da AND a OR '''
    parser = qparser.QueryParser("content", schema=ix.schema, group=qparser.OrGroup)
    query = parser.parse(query_espansa)

    results = searcher.search(query)

    if len(results) == 0:
        finestra.insert(tk.INSERT, "Nessun risultato\n")
    else:
        for x in results:
            finestra.insert(tk.INSERT, str(x) + '\n')


    if len(results) == 0:
        print("Empty result!!")
    else:
        #Apri il file in scrittura
        if not os.path.exists("Risultati"):
            os.mkdir("Risultati")
        stringa = re.sub(r' ',r'_',text)
        stringa1 = re.sub(r'\n',r' ',stringa)
        completeName = os.path.join(os.path.join(os.getcwd(),"Risultati"),stringa1+".txt")
        file = open(completeName,"w")
        for x in results:
            print(x)
            file.write(x["title"]+"\n")
        file.close()

#Creazione della classe GUI
class GUI:
    #Costruttore: inizialmente creo una finestra 800x400
    def __init__(self, ix):
        self.root = tk.Tk()
        self.root.title("Progetto")
        self.root.geometry("800x400")
        self.indice = ix

    #Definizione del metodo start: inizializzo i widget e avvio la finestra
    def start(self):
        self.inizializza()
        self.root.mainloop()

    #Inizializzo i widget
    def inizializza(self):
       self.panel1 = tk.PanedWindow(self.root)
       self.cerca = tk.Button(self.panel1, text = "Cerca", command = lambda: azione(self))
       self.pulisci = tk.Button(self.panel1, text = "Nuova ricerca", command = lambda: pulisci(self))
       self.entry = tk.Entry(self.panel1,width=60)

       #Aggiunta componenti ai pannelli
       self.panel1.add(self.entry)
       self.panel1.add(self.cerca)
       self.panel1.add(self.pulisci)

       self.Scrolledtext1 = tkst.ScrolledText(self.root)
       self.Scrolledtext1.config(state= "disable")

       self.panel1.pack(side = tk.TOP)
       self.Scrolledtext1.pack(fill=tk.BOTH, expand=1)


if ( __name__ == "__main__"):
   try:
       ix = open_dir('indexdir')
   except:
       print("Devi prima creare l'indice")
   finally:
       windows = GUI(ix)
       windows.start()
