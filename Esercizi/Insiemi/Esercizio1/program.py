def es18(d1, d2):
    '''
    Es 9: 3 punti
    Si definisca la  funzione es18(d1,d2) che, 
    - riceve due dizionari aventi per chiavi degli interi e per attributo insiemi di interi.
    - restituisce un dizionario.
    il dizionaro deve contenere come chiavi le chiavi che sono in comune ad entrambi i dizionari e come 
    attributo una tupla di due elementi, il primo elemento e' 
    l'insieme intersezione degli attributi della chiave nei due dizionari mentre 
    il secondo e' l'unione degli attributi della chiave nei due dizionari.
    Ad ESEMPIO se
    d1={1: {1,2,3}, 2:{1,2,3}, 5:{1} } e 
    d2={1: {3,4,5}, 3:{1,2,3}, 5:{3}, 8: {6} }
    allora la funzione  restituisce il dizionario 
    {1: ({3}, {1, 2, 3, 4, 5}), 5: (set(), {1, 3})}
    '''
    k1 = {key for key in d1.keys()}
    k2 = {key for key in d2.keys()}
    k = k1.intersection(k2)
    d = {}
    for key in k:
        t1 = d1[key].intersection(d2[key])
        t2 = d1[key].union(d2[key])
        d[key] = (t1,t2)
    return d    
    pass
