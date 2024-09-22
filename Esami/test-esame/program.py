################################################################################
################################################################################
################################################################################

""" Operazioni da svolgere PRIMA DI TUTTO:
 1) Salvare questo file come program.py
 2) Indicare nelle variabili in basso il proprio
    NOME, COGNOME e NUMERO DI MATRICOLA"""

nome        = "Daniel"
cognome     = "Di Nella"
matricola   = "1997273"

################################################################################
################################################################################
################################################################################
# SUGGERIMENTI PER IL DEBUG 
#   per eseguire solo parte dei test commentare le righe 288-292 alla fine di grade.py
#
#   per vedere lo stack trace degli errore scommentate la riga 36 di testlib.py 
################################################################################
################################################################################
################################################################################

'''Es 1: punti 6

Un file di testo contiene una sequenza di interi separati tra loro da
spazi e andate a capo.  Il file codifica una matrice di interi.

Il primo intero del file riporta il numero di righe di M e il secondo
intero riporta il numero di colonne di M. I numeri seguenti riportano
gli elementi della matrice ordinati per colonne e a parita' per righe.
Si guardi ad esempio il file 'mat1.txt' che codifica la matrice

1 2 
3 4 
5 6  

Progettare una funzione es1(ftesto) che prende in input l'indirizzo di
un file di testo siffatto e restituisca la matrice codificata
rappresentanta tramite lista di liste di interi.
 

Ad esempio, nel caso del file 'mat1.txt'  la funzione deve restituire 
[[1,2],[3,4],[5,6]]

'''

def es1(fname):
    # inserisci qui il tuo codice
    with open(fname) as F:
        testo = F.read()
    lista = testo.split()
    for el in range(len(lista)):
        lista[el] = int(lista[el])
    m = [[0 for i in range(lista[1])] for j in range(lista[0])]
    lista = lista[2:]
    for c in range(len(m[0])):
        for r in range(len(m)):
            m[r][c] = lista[0]
            lista = lista[1:]
    return m
    
    pass
    
#####################################################################################


''' Es 2: punti 7
    
Abbiamo immagini che contengono su sfondo nero rettangoli di diversi
colori che non si intersecano e i cui lati sono segmenti orizzontali o
verticali.  Si consideri ad esempio la figura Rettangoli.png.  Dato un
intero k vogliamo individuare i pixel dell'immagine che hanno come
vicini pixel di esattamente k diversi colori.

Si ricorda che ogni pixel ha potenzialmente 8 vicini: 2 in
orizzontale, due in verticale e 4 in diagonale.

Progettare la funzione es2(fname) che prende come parametro l' ntero k
e l'indirizzo di un file .PNG contenente un'immagine siffatta e
restituisce un dizionario.  Il dizionario contiene:
- come chiavi le tuple di k colori e
- come valore per una chiave l'insieme di pixel dell'immagine che
  hanno come vicini k pixel con quei colori. 
I colori delle chiavi sono rappresentati tramite triple RGB e
compaiono nella tupla in ordine lessicografico crescente. I pixel
negli insiemi-attributo sono rappresentati tramite le tuple con le
loro coordinate (colonna, riga)
    
Ad esempio per il file Rettangoli.png e k=4 la funzione e2 deve restituire il dizionario
{((0, 0, 255), (0, 255, 0), (100, 100, 100), (255, 0, 0)): {(39, 60), (39, 59), (40, 59), (40, 60)} }

Per caricare e salvare i file PNG si possono usare load e save della
libreria images.  '''

import images

def es2(k,fname1):
    im = images.load(fname1)
    diz = {}
    for r in range(len(im)):
        for c in range(len(im[0])):
            x = 1
            y = 2
            w = 1
            z = 2
            p = im[r][c]
            lista = [p]
            if r == 0:
                x = 0
                y = 2
            if c == 0:
                w = 0
                z = 2
            if r == len (im)-1:
                x = 1
                y = 1
            if c == len(im[0])-1:
                w = 1
                z = 1
            for r2 in range(r-x,r+y):
                for c2 in range(c-w,c+z):
                    p2 = im[r2][c2]
                    if p != p2 and p2 not in lista:
                        lista.append(p2)
            if len(lista) == k:
                lista.sort()
                tupla = tuple(lista)
                if tupla not in diz:
                    diz[tupla] = {(c,r)}
                else:
                    valore = list(diz[tupla])
                    valore += [(c,r)]
                    diz[tupla] = set(valore)
    return diz
    
    
    pass


############################################################################


'''
Es. 3: punti 10

Si definisca la funzione es3(r) ricorsiva (o che fa uso di funzioni o
metodi ricorsive/i) che riceve come parametro la radice r di un albero
binario formato da nodi del tipo AlberoBinario definito nella libreria
albero.py e restituisce una lista di tuple.

La lista contiene una tripla per ogni nodo x dell'albero, piu'
precisamente per ogni nodo x dell'albero:
- la prima coordinata della tripla riporta il valore del nodo x,
- la seconda coordinata riporta il numero di nodi discendenti di x con
  valore inferiore al valore di x
- la terza coordinata riporta il numero di nodi discendenti di x con
  valore superiore al valore di x Le triple della lista devono
  risultare ordinate lessicograficamente.

Ad esempio per l'albero:
     0
    / \
   1   5 
      / 
     3
    / \ 
   9   7

   
la funzione es3 restituisce la lista 
[(0, 0, 5), (1, 0, 0), (3, 0, 2), (5, 1, 2), (7, 0, 0), (9, 0, 0)]


NOTA: definite le vostre sottofunzioni a livello esterno altrimenti
          non passate il test di ricorsione '''


import albero

def es3(r):
    # inserisci qui il tuo codice
    lista = svolgi(r)
    return sorted(lista)


def svolgi(r):
    l1 = []
    l2 = []
    l3 = []
    p = 0
    m = 0
    if r.dx != None or r.sx != None:
        if r.dx != None:
            l2 = svolgi(r.dx)
            for el in l2:
                if r.valore < el[0]:
                    m += 1
                elif r.valore > el[0]:
                    p += 1
        if r.sx != None:
            l3 = svolgi(r.sx)
            for el in l3:
                if r.valore < el[0]:
                    m += 1
                elif r.valore > el[0]:
                    p += 1
        l1 = l2 + l3 + [(r.valore,p,m)]
    else:
        l1 = [(r.valore,0,0)]
    return l1
    pass


  
###########################################################################

'''
Es. 4: punti 9
    
Si realizzi la funzione ricorsiva (o che usa funzioni ricorsive)
es(dirname, insieme) che riceve come argomento il nome di una
directory (dirname) ed un insieme di stringhe (insieme).  La funzione
esplora la directory dirname e le sue sottodirectory e restituisce il
numero di file che incontra aventi come estensione una delle stringhe
dell'insieme. Si devono ignorare tutti i file e directory che iniziano
con '.'  oppure '_'
    
Ad esempio con dirname='dir1' e insieme={'txt','pdf'} la funzione es4
deve restituire il numero 5

NOTA: è proibito usare la funzione os.walk

NOTA: definite le vostre sottofunzioni a livello esterno altrimenti
          non passate il test di ricorsione '''    

import os
def es4(dirname,insieme): 
    # inserisci qui il tuo codice
    count = 0
    for name in os.listdir(dirname):
        if '.' == name[0] or '_' == name[0]: continue
        fn = dirname + '/' + name
        if os.path.isdir(fn):
            count += es4(fn,insieme)
        else:
            for ext in insieme:
                if fn.endswith(ext):
                    count += 1
    return count
    pass

