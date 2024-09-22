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
# ---------------------------- SUGGERIMENTI PER IL DEBUG --------------------- #
# Per eseguire solo alcuni dei test, si possono commentare le voci con cui la
# lista 'test' è assegnata alla fine di grade.py
#
# Per controllare lo stack trace degli errori, si può decommentare la linea
# dedicata in testlib.py (vedere il commento nel corpo della funzione runOne)
################################################################################


# ----------------------------------- EX.1 ----------------------------------- #
'''Es1: 7 punti
    Si scriva una funzione ex1(file_rows, file_cols, file_values) che
    prende in ingresso i percorsi di 3 file e restituisca in output
    una matrice, rappresentata come lista di liste.  Scopo
    dell'esercizio è ricostruire la matrice di output ("out") calcolata in base
    alle tre matrici ("rows", "cols" e "values") salvate nei file di input
    (rispettivamente: file_rows, file_cols, file_values).

    I file contengono su diverse righe dei numeri interi separati da
    spazi: ogni riga del file è una riga della matrice ed il
    c-esimo numero su una data riga corrisponde al c-esimo elemento
    (la colonna c) della riga corrispondente.  Ad esempio, se il file
    contiene:

    0    1
    1 0

    la matrice codificata come lista di liste è:

    [[0, 1],
    [1, 0]].

    La matrice "out" da restituire ha nella posizione (r,c) l'elemento
    della matrice "values" individuato dalla riga indicata dal valore
    nella posizione (r,c) della matrice "rows" e dalla colonna
    indicata dal valore nella posizione (r,c) della matrice
    "cols". Nel caso in cui gli indici ricavati da "rows" e "cols" non
    individuino un elemento valido nella matrice "values" (ad esempio,
    indice negativo o indice fuori dal numero righe o degli elementi
    di una riga), la matrice "out" deve contenere None nella posizione
    corrispondente.

    Ad esempio: dati i tre file di ingresso che codificano le matrici
          "rows"              "cols"                     "values"
     0         1        |   1              5    |     3     4      1
     0         1        |   0              2    |     10     -1    5

    si deve restituire:

      "out"
    [[4, None],
     [3, 5]]

    Si noti che:
    - alla posizione di "out" (1,1) vi è 5 che si trova in "values" alla
      riga indicata da "rows" alla posizione (1,1) (ossia 1) e colonna
      indicata da "cols" alla posizione (1,1) (ossia 2);
    - alla posizione di "out" (0,1) vi è None perché "values" non è
      accessibile con indice (1,5).

    Nota: "out", "rows" e "cols" hanno stesse dimensioni fra loro,
          mentre "values" può avere dimensioni diverse.

'''

def ex1(file_rows, file_cols, file_values):
    # Inserire qui il proprio codice
    with open(file_rows) as R:
        rows = R.readlines()
    for i in range(len(rows)):
        rows[i] = rows[i].split()
        
    with open(file_cols) as C:
        cols = C.readlines()
    for i in range(len(cols)):
        cols[i] = cols[i].split()
        
    with open(file_values) as V:
        values = V.readlines()
    for i in range(len(values)):
        values[i] = values[i].split()

    out = [[None for i in range(len(rows[0]))] for j in range(len(rows))]

    for i in range(len(rows)):
        for j in range(len(rows[0])):
            r = int(rows[i][j])
            c = int(cols[i][j])
            if r < len(values) and r >= 0 and c < len(values[0]) and c >= 0:
                out[i][j] = int(values[r][c])
    return out

# ----------------------------------- EX.2 ----------------------------------- #

'''Es2: 8 punti

    Data una immagine PNG con dei rettangoli di colore bianco su uno
    sfondo di colore nero, si vuole sommare tra loro i perimetri di
    tutti i rettangoli che hanno i lati orizzontali della stessa
    lunghezza, intesa come numero di pixel. I rettangoli non si
    incontrano né si toccano in nessun punto.

    Si progetti la funzione ex2(input_file) che prende in input un file
    con una immagine PNG come descritto sopra e resituisce un
    dizionario. Il dizionario ha:

    - per chiavi, le diverse lunghezze dei lati orizzontali dei
      rettangoli

    - per valori, le somme dei perimetri dei rettangoli che hanno il
      lato orizzontale della lunghezza pari alla chiave.

    Esempio: poiché l'immagine nel file ex2p1.png contiene due
      rettangoli con base 20 pixel e altezza 10 pixel e un rettangolo
      3x3, la funzione ex('ex2p1.png') deve restituire il dizionario:
      {20: 120, 3:12}
'''

import images
def ex2(input_file):
    im = images.load(input_file)
    d = {}
    for r in range(len(im)):
        for c in range(len(im[0])):
            if im[r][c] == (255,255,255):
                l,h,im = perimetro(im,r,c)
                #print (l,h,r,c)
                if l in d:
                    d[l] += (l*2)+(h*2)
                else:
                    d[l] = (l*2)+(h*2)
    return d
    pass
    
def perimetro(im,r,c):
    l = 0
    h = 0
    r2 = r
    c2 = c
    while im[r][c] == (255,255,255) and c < len(im[0])-1:
        im[r][c] = (255,0,0)
        l+=1
        c+=1
    c -= 1
    im[r][c] = (255,255,255)
    while im[r][c] == (255,255,255) and r < len(im)-1:
        im[r][c] = (255,0,0)
        h+=1
        r+=1
    for i in range(h):
        for j in range(l):
            im[r2+i][c2+j] = (255,0,0)
    return l,h,im

# ----------------------------------- EX.3 ----------------------------------- #

'''Es3: 9 punti
    Si progetti la funzione ex3 ricorsiva o che fa uso di funzioni o metodi
    ricorsivi che riceve come argomento una stringa di caratteri e restituisce
    le foglie dell'albero di gioco ottenuto applicando la seguente mossa:
    - eliminare dalla stringa una coppia di caratteri consecutivi diversi
        ma ignorando la differenza tra maiuscole e minuscole.
    Le foglie sono le stringhe alle quali non è più possibile applicare la
    mossa.
    La funzione deve restituire una lista di foglie, senza ripetizioni ed in
    ordine decrescente di lunghezza ed, a parimerito, in ordine alfabetico
    crescente.

    Esempio: se la stringa è 'aBbACc' l'albero di gioco (indentato) sarà:

aBbACc
    bACc            # eliminati 'aB'
        Cc          # eliminati 'bA' (foglia)
        bc          # eliminati 'AC'
           ''       # eliminati 'bc' (foglia)
    aBCc            # eliminati 'bA'
        Cc          # eliminati 'aB' (foglia)
        ac          # eliminati 'BC'
           ''       # eliminati 'ac' (foglia)
    aBbc            # eliminati 'AC'
        bc          # eliminati 'aB'
           ''       # eliminati 'bc' (foglia)
        aB          # eliminati 'bc'
           ''       # eliminati 'aB' (foglia)

     Quindi il risultato da restituire sarà la lista [ 'Cc', '' ]

'''

class Albero:
    def __init__(self,v,sons = None):
        self.v = v
        self.sons = sons


def ex3(stringa):
    a = crea(stringa)
    lista = esplora(a)
    return a
    lista2 = []
    for i in lista:
        if i not in lista2:
            lista2.append(i)
    return lista2
    
    
    
def crea(stringa):
    if len(stringa) == 0 or stringa.count(stringa[0].lower())==len(stringa):
        return Albero(stringa)
    else:
        sons = []
        for i in range(1,len(stringa)-1):
            if stringa[i].lower() != stringa[i-1].lower():
                s = stringa.replace(stringa[i-1:i+1],'')
                sons.append(crea(s))
            elif stringa[i].lower() != stringa[i+1].lower():
                s = stringa.replace(stringa[i:i+2],'')
                sons.append(crea(s))     
    return Albero(stringa,sons)
    pass
    # Inserire qui il proprio codice

def esplora(a):
    if a.sons == None:
        return a.v
    else:
        lista = []
        for foglia in a.sons:
            if foglia.sons == None:
                lista.append(esplora(foglia))
            else:
                lista += esplora(foglia) 
    return lista

# ----------------------------------- EX.4 ----------------------------------- #

'''Es4: 8 punti

    Si progetti la funzione ex4 ricorsiva o che fa uso di funzioni
    ricorsive, che prende come parametri di input il path di una
    directory 'dir1' e una stringa 'ext'. La funzione deve
    esplorare l'albero delle directory a partire dalla directory 'dir1'
    e ritornare un dizionario così fatto:

    - le chiavi sono stringhe, una per ogni sotto-directory di 'dir1'
      che contiene almeno un file il cui nome inizia con una lettera
      maiuscola e che ha estensione 'ext';

    - i valori sono liste di stringhe (una stringa per ogni file
      presente nella sotto-directory della chiave) il cui nome inizi
      con una lettera maiuscola e che termini con estensione
      'ext'. Le liste sono ordinate per numero di caratteri
      componenti le stringhe e, in caso di parità, ordine alfabetico.

    Esempio: la funzione ex4('ex4/a0','.txt') deve tornare il dizionario
      {
       'ex4/a0': ['Roar.txt', 'Miaao.txt', 'Muuuu.txt'],
       'ex4/a0/b1': ['Bau.txt', 'Ciao.txt', 'Miao.txt']
      }

    Si suggerisce di usare la funzione os.listdir e le funzioni del
    modulo os.path. La funzione os.path.join potrebbe non funzionare
    in Windows, si suggerisce di usare la concatenazione con il
    carattere '/'.

    NOTA: è proibito usare la funzione os.walk 
'''
import os

def ex4(dir1, ext):
    d = {}
    for name in os.listdir(dir1):
        fn = dir1 + '/' + name
        if os.path.isdir(fn):
            d2 = ex4(fn,ext)
            for key in d2.keys():
                if key in d:
                    d[key] += d2[key]
                else:
                    d[key] = d2[key]
        else:
            if name[0].isupper() and fn.endswith(ext):
                if dir1 in d:
                    d[dir1].append(name)
                else:
                    d[dir1] = [name]
    for chiave in d.keys():
        d[chiave] = sorted(d[chiave],key=len)
    return d
    
    
    
    pass
    # inserire qui il proprio codice
