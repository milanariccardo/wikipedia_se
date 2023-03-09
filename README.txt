Il progetto è stato realizzato da il gruppo composto da Barbanti Francesco (matricola 112374) e Milana Riccardo (matricola 113180). 
La versione di Python utilizzata è Python 3.8.1 
Le librerie utilizzate sono:
 - sax
 - nltk
 - whoosh
 - Tkinter
 - Numpy
 - Matplotlib

All'interno della cartella "Progetto gestione dell'informazione" sono contenuti i seguenti file:
 - Dump.xml che contiene il Dump utilizzato per il test del Search Engine (contiene i primi 30 risultati delle 30 query di test, quindi un totale di 900 documenti)
 - index.py consente di creare l'indice
 - query.py consente di effettuare query
 - evaluation.py consente di calcolare la MAP e produce i grafici di NDCG e Average Precision ai vari livelli di recall
 - la cartella indexdir contente l'indice creato

Per l'esecuzione eseguire in ordine:
- python index.py "percorso file Dump"  ---> solo se si vuole ricreare l'indice, in quanto viene sovrascritta la cartella indexdir. La creazione dell'indice richiede circa 20 minuti. Se non si vuole ricreare, nella cartella indexdir è già presente l'indice del Dump completo. 
- python query.py 
- python evaluation.py ---> per la valutazione, le query inserite devono rispettare maiuscole, minuscole e spazi (devono essere esattamente quelle presenti nel pdf), in quanto per ogni query viene creato un file "\Risultati\query.txt". Se tale file non viene trovato, si assume che la query non abbia ritornato documenti. La valutazione viene fatta considerando le 30 query.
