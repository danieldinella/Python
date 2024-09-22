################################################################################
################################################################################
################################################################################

''' ATTENZIONE!!! INSERITE SUBITO QUI SOTTO IL VOSTRO NOME, COGNOME E MATRICOLA '''

nome        = "Daniel"
cognome     = "Di Nella"
matricola   = "1997273"

################################################################################
################################################################################
################################################################################
# SUGGERIMENTI PER IL DEBUG 
#   per eseguire solo parte dei test commentare parte della lista "tests"
#   alla fine di grade.py
#
#   per vedere lo stack trace degli errore scommentate la riga 36 di testlib.py 
################################################################################
################################################################################
################################################################################

''' 
    Es 1: punti 7 
    Le righe di un file di testo contengono uno o piu' interi separati
    da spazi. Progettare una funzione es1(ftesto) che, prende in input
    l'indirizzo di un file di testo siffatto e restituisce una lista
    di coppie di interi.  La lista contiene tante coppie quante sono
    le righe del file.  La riga i-esima della lista contiene la coppia
    che ha come prima coordinata la somma degli interi nella riga
    i-esima del file e come seconda coordinata il prodotto degli
    interi nella riga i del file. 
    
    Ad Esempio, per il file di testo
    f1.txt la funzione restituisce la lista: [(7,8), (11,30), (8,8), (6,8)]
'''

def es1(fname):
    # inserisci qui il tuo codice
    with open(fname) as F:
        righe = F.readlines()
    for i,r in enumerate(righe):
        righe[i] = r.split()
    lista = []
    for i in range(len(righe)):
        s = 0
        p = 1
        for j in range(len(righe[i])):
            s += int(righe[i][j])
            p *= int(righe[i][j])
        lista.append((s,p))
    return lista
    pass
        
#####################################################################################


'''    
    Es 2: punti 8
    
    Abbiamo un'immagine dove su sfondo nero sono disegnati in bianco
    rettangoli e quadrati che non si toccano ne si intersecano e i cui
    lati sono segmenti orizzontali o verticali.  Si veda ad esempio
    l'immagine in fig1.png.  Vogliamo trovare il numero di quadrati ed
    il numero di rettangoli presenti nell'immagine.
   
    Progettare la funzione es2(fname) che prende come parametro
    l'indirizzo di un file .PNG contenente l'immagine e restituisce la
    coppia di interi (x,y) dove x e' il numero di quadrati presenti
    nell'immagine e y il numero di rettangoli presenti nell'immagine.
    Ad esempio per l'immagine fig1.png la funzione deve restituire la
    coppia (3,2).
        
    Per caricare e salvare i file PNG si possono usare load e save
    della libreria immagini.
    '''

import immagini

def es2(fname1):
    # inserisci qui il tuo codice
    im = immagini.load(fname1)
    x = 0
    y = 0
    for r in range(len(im)):
        for c in range(len(im[0])):
            if im[r][c] == (255,255,255):
                im,z = definisci(im,r,c)
                if z == True:
                    x += 1
                else:
                    y += 1
    return(x,y)
                
    pass


def definisci(im,r,c):
    w = 0
    h = 0
    r2 = r
    c2 = c
    while c<len(im[0]) and im[r][c] == (255,255,255):
        im[r][c] = (0,0,0)
        w += 1
        c += 1
    c -= 1
    im[r][c] = (255,255,255)
    while r<len(im) and im[r][c] == (255,255,255):
        im[r][c] = (0,0,0)
        h+=1
        r+=1
    r -= 1
    im[r][c] = (0,0,0)
    for i in range(r2,r+1):
        im[i][c2] = (0,0,0)
    for j in range(c2,c+1):
        im[r][j] = (0,0,0)
    if h == w:
        return im,True
    else:
        return im,False


############################################################################


'''
    Es. 3: punti 8
   
    Si definisca la funzione es3(r1,r2) ricorsiva (o che fa uso di
    funzioni o metodi ricorsive/i) che riceve come parametri le radici
    r1 ed r2 di due alberi binari formati da nodi del tipo
    AlberoBinario definito nella libreria albero.py. I due alberi sono
    identici se non per il fatto che il valore di nodi corrispondenti
    non sempre coincide.  La funzione deve restituire una lista di
    coppie, una coppia per ogni coppia di nodi che non hanno lo stesso
    valore. La coppia contiene il valore del nodo del primo albero
    come prima coordinata ed il valore del nodo del secondo albero
    come seconda coordinata.  Le coppie nella lista devono risultare
    ordinate in modo decrescente.

    Ad esempio per gli alberi :
         0            0
        / \          / \
       5   6        5   1
          /            /
         3            3
        / \          / \
       9   7        2   7

    la funzione es3 restituisce la lista [(9,2), (6,1)]


    NOTA: definite le vostre sottofunzioni a livello esterno
          altrimenti non passate il test di ricorsione
`'''


import albero

def es3(r1,r2):
    # inserisci qui il tuo codice
    lista = []
    if r1.sx != None:
        lista += es3(r1.sx,r2.sx)
    if r1.dx != None:
        lista += es3(r1.dx,r2.dx)
    if r1.valore != r2.valore:
        lista.append((r1.valore,r2.valore))
    return sorted(lista,reverse = True)
    pass
  
###########################################################################


'''
    Es. 4: punti 9
    
    Si realizzi la funzione ricorsiva (o che usa funzioni ricorsive)
    es(dirname) che riceve come argomento il nome di una directory
    (dirname) ed una stringa (s).  La funzione esplora la directory
    dirname e le sue sottodirectory alla ricerca di file con
    estensione .txt e restituisce un dizionario.  Le chiavi del
    dizionario sono tutte le stringhe trovate nei file .txt che hanno
    come sottostringa la stringa s. Attributo di ciascuna chiave e' il
    numero di volte per cui quella parola appare nei file .txt.
    Ignorate tutti i file e directory che iniziano con '.' oppure '_'
    
    Ad esempio con dirname='dir1'  e s='arco' la funzione 
    es4 deve restituire il dizionario:
    {'parco': 1, 'arco': 3, 'Marco': 1, 'sarcofago': 1}
   
    NOTA: è proibito usare la funzione os.walk
    NOTA: definite le vostre sottofunzioni a livello esterno
          altrimenti non passate il test di ricorsione
'''    

import os
def es4(dirname,s):
    # inserisci qui il tuo codice
    d = {}
    for name in os.listdir(dirname):
        if name[0] == '.' or name[0] == '_': continue
        fn = dirname + '/' + name
        if os.path.isdir(fn):
            d2 = es4(fn,s)
            for key in d2.keys():
                if key in d:
                    d[key] += d2[key]
                else:
                    d[key] = d2[key]
        else:
            if fn.endswith('txt'):
                with open(fn) as F:
                    testo = F.read()
                testo = testo.split()
                for parola in testo:
                    if s in parola:
                        if parola in d:
                            d[parola] += 1
                        else:
                            d[parola] = 1
    return d
    pass
