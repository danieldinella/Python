'''
      Es 2: 6 punti
      Si definisca la funzione es14(tree,x) ricorsiva (o che fa uso di funzioni o metodi ricorsive/i) 
      che riceve come argomenti:
      -  'tree' un  albero  formato da nodi di tipo AlberoBinario definito nella libreria 
          albero.py allegata
      - un intero x
      - calcola il numero di nodi che nell'albero che hanno valore divisibile per x 
      - torna come risultato il numero calcolato

      ATTENZIONE: E' VIETATO USARE I METODI DELLA LIBRERIA albero

      Esempio: se x = 2 e l'albero e':

              7
              /\
            1  3
            / \
          4    6
        /    /
        5    2
      /     \
      9       8

  Nell'albero ci sono 3 nodi con valore divisibile per 2+livello (sono i nodi a valore 3,4 e 5)
  cosi'  la funzione tornera' il valore 3.
'''

import albero
def es14(tree, x):
    if tree.sx == None and tree.dx == None:
        if tree.valore % x == 0:
            return 1
        else:
            return 0
    else:
        risultato = 0
        if tree.sx != None:
            risultato += es14(tree.sx,x+1)
        if tree.dx != None:
            risultato += es14(tree.dx,x+1)
        if tree.valore % x == 0:
            risultato += 1
        return risultato
            



