

import albero

'''
    Es 12: 3 punti
    Un albero si dice binario completo se tutti i suoi nodi interni hanno esattamente 2 
    figli e tutte le foglie si trovano allo stesso livello.
    Si definisca la funzione es12(k ) ricorsiva (o che fa uso di funzioni o 
    metodi ricorsive/i) che:
    - riceve come argomenti  un intero k 
    - costruisce un albero binario completo di altezza k composta da nodi del tipo  
      Nodo definito nella libreria albero.py allegata. Gli identificatore delle foglie, 
      letti da sinistra a destra sono i 2^k-interi che vanno da 1 a 2^k (nota che 
      un albero binario completo di altezza k ha sempre 2^k foglie). Gli identificatori 
      dei nodi interni sono dati dalla somma degli identificatori dei due loro figli. 
    - torna come risultato la radice dell'albero costruito. 
    Esempio: 
    - es12(2)  crea e restituisce l'albero a sinistra 
    - es12(3) crea e restituisce l'albero a destra


                    10                                  36               
             _______|______                      _______|______         
            |              |                    |              |        
            3              7                   10             26        
         ___|___        ___|__               ___|___        ___|__      
        |       |      |      |             |       |      |      |     
        1       2      3      4             3       7     11     15     
                                           _|_     _|_    _|_    _|_    
                                          |   |   |   |  |   |  |   |   
                                          1   2   3   4  5   6  7   8   
                                                                   
    '''

class Nodo:
    def __init__(self,V):
        self.id=V
        self.f=[]
        
def genera_albero(lista,k,livello):
    if livello == k:
        nodo = Nodo(lista[0])
        return nodo,lista[1:]
    else:
        somma = 0
        for i in range(2):
            nodo,lista = genera_albero(lista,k,livello+1)
            somma += nodo.id
        return Nodo(somma)
    
        
        

def es1(k):
    # inserisci qui il tuo codice
    lista = [i for i in range(1,(k**2)+1)]
    radice = genera_albero(lista, k, 0)
    return radice.id    
    
    pass
    
