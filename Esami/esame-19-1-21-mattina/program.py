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
#   per eseguire solo parte dei test commentare alcune righe 399-403 alla fine di grade.py
#
#   per vedere lo stack trace degli errore scommentate la riga 36 di testlib.py 
################################################################################
################################################################################
################################################################################

'''
Esercizio 1: 6 punti

Sia data una tabella rappresentata come lista di dizionari.
Ciascuna colonna della tabella è individuata dal suo nome.
Ciascun dizionario contenuto nella lista ha le stesse chiavi, che sono i nomi delle colonne della tabella.
I valori possono essere stringhe, interi o float.

Esempio: la tabella
    Nome    Cognome     Telefono    Indirizzo
    Andrea  Sterbini    137487468   via del Pero 3
    Gianni  Rodari      137487468   via degli Angeli 14
    Gianni  Pierini     137487468   via degli Angeli 17
Corrisponde alla lista di dizionari
[   { 'Nome': 'Andrea', 'Cognome': 'Sterbini', 'Telefono': 137487468, 'Indirizzo': 'via del Pero 3' },
    { 'Nome': 'Gianni', 'Cognome': 'Rodari',   'Telefono': 137487468, 'Indirizzo': 'via degli Angeli 14' },
    { 'Nome': 'Gianni', 'Cognome': 'Pierini',  'Telefono': 137487468, 'Indirizzo': 'via degli Angeli 17' },
]

Si progetti la funzione es1(tabella, colonne, elimina) che riceve come argomenti:
    - tabella: una tabella rappresentata come lista di dizionari
    - colonne: una lista di nomi di colonne rispetto alle quali ordinare la tabella
    - elimina: una lista di nomi di colonne che vanno completamente eliminate
e che torna come risultato il numero di colonne eliminate.
Le righe della tabella devono risultare ordinate in ordine crescente (distruttivamente)
relativamente al sottoinsieme di valori presenti nelle colonne indicate.
Inoltre tutte le colonne indicate nella lista 'elimina' devono essere eliminate.

Esempio: se colonne=['Nome', 'Cognome'] e elimina=['Telefono'] la tabella deve diventare
[   { 'Nome': 'Andrea', 'Cognome': 'Sterbini', 'Indirizzo': 'via del Pero 3' },
    { 'Nome': 'Gianni', 'Cognome': 'Pierini',  'Indirizzo': 'via degli Angeli 17' },
    { 'Nome': 'Gianni', 'Cognome': 'Rodari',   'Indirizzo': 'via degli Angeli 14' }
]

Esempio: se colonne=['Telefono', 'Nome', 'Indirizzo'] la tabella deve diventare
[   { 'Nome': 'Andrea', 'Cognome': 'Sterbini', 'Telefono': 137487468, 'Indirizzo': 'via del Pero 3' },
    { 'Nome': 'Gianni', 'Cognome': 'Rodari',   'Telefono': 137487468, 'Indirizzo': 'via degli Angeli 14' },
    { 'Nome': 'Gianni', 'Cognome': 'Pierini',  'Telefono': 137487468, 'Indirizzo': 'via degli Angeli 17' },
]

NOTA: se colonne=[] la tabella deve rimanere invariata.
NOTA: se elimina=[] non deve essere eliminata nessuna colonna.

'''
def es1(tabella, colonne, elimina):
    tabella.sort(key=lambda x: [x[colonna] for colonna in colonne] )
    for riga in tabella:
        for colonna in elimina:
            del riga[colonna]
    return len(elimina)
    # inserisci qui il tuo codice

#################################################################################################

'''
Es 2: punti 8

Sia dato un file PNG contenente una immagine.
Si realizzi la funzione es2(file_png, colori) che riceve come argomenti:
    - file_png: il filename del file PNG
    - colori:   una lista di colori RGB (tuple di 3 valori tra 0 e 255)
che trova i bounding-box dei pixel che sono colorati con ciascuno dei colori 
(il bounding-box è la tupla  (x1,y1,x2,y2) del punto più in alto a sinistra x1,y1 
e del più in basso a destra x2,y2 che contiene tutti i pixel di quel colore)
La funzione deve infine tornare la lista dei bounding-box ordinata per area decrescente,
e in caso di parità in ordine crescente di colore.
NOTA: se il colore non appare nell'immagine il valore da tornare per quel colore è None e l'area è 0.
Esempio: se la immagine è '3cime.png' 
    ed i colori sono [ (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 200, 200) ]
Il risultato sarà:
    [(137, 10, 191, 31), (95, 121, 95, 121), (149, 47, 149, 47), None]
'''
import images

def es2(file_png, colori):
    im = images.load(file_png)
    lista = []
    for colore in colori:
        x1,y1,x2,y2 = None,None,None,None
        for r in range(len(im)):
            for c in range(len(im[0])):
                if im[r][c] == colore:
                    if  y1 == None or r < y1:
                        y1 = r
                    if y2 == None or r > y2:
                        y2 = r
                    if x1 == None or c < x1:
                        x1 = c
                    if x2 == None or c > x2:
                        x2 = c
        if x1 == None:
            lista.append((0,0,0,0))
        else:
            lista.append(((x2-x1)*(y2-y1),colore[0],colore[1],colore[2],x1,y1,x2,y2))
    lista.sort(key = lambda x: (x[0],x[1],x[2],x[3]), reverse = True)
    for i in range(len(lista)):
        lista[i] = list(lista[i])
        lista[i].pop(0)
        lista[i].pop(0)
        lista[i].pop(0)
        lista[i].pop(0)
        lista[i] = tuple(lista[i])
        if len(lista[i]) == 0:
            lista[i] = None
    return lista
            
        
    pass
    # inserisci qui il tuo codice

#################################################################################

'''
Es 3: punti 9

Si definisca la funzione es3(albero, k), ricorsiva o che fa uso di funzioni/metodi ricorsivi,
che riceve come argomenti:
    - albero: la radice di un albero di tipo tree.BinaryTree (vedi tree.py)
    - k:      un intero
che per ogni nodo che ha valore ID che è multiplo di k, elimina ricorsivamente tutti figli e nipoti del nodo.
Lo ID del nodo multiplo di k viene sostituito con la somma degli ID dei nodi eliminati.

Esempio:            6
                /       \
            7               5
        /       \       /       \
    2           4       6       8
               /                 \
              15                  10
se k = 5 l'albero diventa
                    6
                /       \
            7               24
        /       \       
    2           4      
               /
              0
'''
import tree
def es3(albero, k):
    return elimina(albero,k,False)
    pass
    # inserisci qui il tuo codice
    
def elimina(albero,k,x):
    somma = 0
    if x == True:
        if albero.left != None:
            somma += elimina(albero.left,k,x)
        if albero.right != None:
            somma += elimina(albero.right,k,x)
        somma += albero.ID
        return somma
    else:
        if albero.ID % k == 0:
            if albero.left != None:
                somma += elimina(albero.left,k,True)
                albero.left = None
            if albero.right != None:
                somma += elimina(albero.right,k,True)
                albero.right = None
            albero.ID = somma
            return albero
        else:
            if albero.left != None:
                albero.left = elimina(albero.left,k,x)
            if albero.right != None:
                albero.fight = elimina(albero.right,k,x)
            return albero
            
            

###############################################################################
'''
Esercizio 4: 9 punti

Si dato un albero N-ario formato da nodi tree.NaryTree.

Realizzate la funzione es4(radice, k) che riceve come argomenti:
    - radice: un nodo di tipo tree.NaryTree
    - k: il numero minimo di figli da cercare
e che trova i due nodi che hanno almeno k figli ed hanno profondità massima e minima
e torna come risultato la tupla
    (differenza_di_profondita, differenza_di_valore)
NOTA: potete assumere che i nodi con almeno k figli che sono a profondità massima e minima sono unici

Esempio:
                          17
                          |
        -------------------------------------------
        |      |          |         |             |
        13     21        95        32            26
        |      |          |                       |
    --------   |     ---------------------        |
    |   |  |   |     |   |   |   |   |   |        |
    4   7  9   5    -3  -4  -5  -6   -8  -10      42

    Se k=4
    - il nodo meno profondo con almeno 4 figli è il 17 che sta a profondità 0
    - il nodo più  profondo con almeno 4 figli è il 95 che sta a profondità 1
    e la funzione deve tornare la tupla (1, 78)
'''

def es4(radice, k):
    inf,sup = calcola(radice,k,0,None,None)
    if inf == None:
        return sup
    elif sup == None:
        return inf
    else:
     return (sup[0]-inf[0],sup[1]-inf[1])
    
    pass
    # inserisci qui il tuo codice

def calcola(radice,k,livello,inf,sup):
    if radice.sons != None:
        if len(radice.sons) >= k:
            if inf == None:
                inf = (livello,radice.value)
                for i in radice.sons:
                    inf,sup = calcola(i,k,livello+1,inf,sup)
            elif sup == None:
                sup = (livello,radice.value)
                for i in radice.sons:
                    inf,sup = calcola(i,k,livello+1,inf,sup)
            else:
                return inf,sup
        else:
            for i in radice.sons:
                inf,sup = calcola(i,k,livello+1,inf,sup)
    return inf,sup
                


if __name__ == '__main__':
    pass
    # inserisci qui i tuoi test
