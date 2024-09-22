# -*- coding: utf-8 -*-
'''Nel gioco "chi la spara più grossa" si sfidano due concorrenti A e
B che generano delle sequenze di valori di lunghezza variabile,
rappresentati da un singolo carattere. Le sequenze possono essere di
lunghezza diversa poiché i valori possono essere separati da uno (o
più) spazi bianchi e tab ('\t'). Il numero di caratteri non spazio è,
comunque, uguale per ogni sequenza.

Ogni elemento della sequenza di A viene confrontato con l'elemento
corrispondente della sequenza di B e viene assegnato un punto
- al concorrente che ha generato il valore più alto (per esempio A),
  se la differenza fra il valore di A e il valore di B è inferiore o
  uguale ad un parametro k deciso all'inizio della sfida
- al concorrente che ha generato il valore più basso (per esempio B),
  se la differenza fra il valore di A e il valore di B è superiore
  a k (cioè A ha sballato)
- a nessuno, in caso di pareggio.
Al termine dell'assegnazione, vince chi ha ottenuto più punti. In caso
di pareggio, vince il giocatore che ha generato la sequenza con somma
totale dei valori inferiore.  In caso di ulteriore pareggio, il punto
è assegnato al giocatore con la prima sequenza in ordine
lessicografico. Non può capitare che due giocatori generino
esattamente la stessa sequenza di valori.

Si deve realizzare una funzione che prende in input il parametro k e
una lista di stringhe corrispondenti a un torneo di "chi la spara più
grossa" e restituisce la classifica finale del torneo. La stringa in
posizione i corrisponde alla sequenza dei valori generati dal
giocatore i.

Nel torneo, ogni giocatore sfida tutti gli altri con la propria
sequenza: ovvero, se ci sono n giocatori, ogni giocatore farà n-1
sfide. Il numero di sfide vinte determina la posizione in
classifica. In caso di parità di sfide vinte, i giocatori sono
ordinati in modo crescente in base alla posizione.

Esempio di partite a chi la spara più grossa fra tre giocatori.
    Se k=2 e la lista è ["aac","ccc","caa"]
        La sfida 0, 1 è vinta da 1 per 2 punti a 0, poiché la
            differenza fra "c" e "a" è inferiore o uguale a 2
        La sfida 0, 2 è un pareggio 1 a 1, le due sequenze hanno somma
            uguale, ma vince 0 perché la sequenza "aac" < "caa".
        La sfida 1, 2 è vinta da 1 per 2 punti a 0, poiché la
            differenza fra "c" e "a" è inferiore o uguale a 2.
        Alla fine 0 ha 1 sfida, 1 ha 2 sfide e 2 ha 0 sfide, per cui
            la classifica finale sarà [1, 0, 2].

    Se k=1 e la lista è ["aac","ccc","caa"]
        La sfida 0, 1 è vinta da 0 per 2 punti a 0, poiché la
            differenza fra "c" e "a" è maggiore di 1.
        La sfida 0, 2 è un pareggio 1 a 1, le due sequenze hanno somma
            uguale, ma vince 0 perché la sequenza "aac" < "caa".
        La sfida 1, 2 è vinta da 2 per 2 punti a 0, poiché la
            differenza fra "c" e "a" è maggiore di 1.
        Alla fine 0 ha 2 sfide, 1 ha 0 sfide e 2 ha 1 sfida, per cui
            la classifica finale sarà [0, 2, 1].

    Se k=10 e la lista è  [ "abc",  "dba" , "eZo"]
        La sfida 0, 1 è un pareggio, ma vince 0 perché la sua sequenza
            ha somma inferiore.
        La sfida 0, 2 è vinta da 0 per 2 punti a 1, perché 2 sballa
            con la lettera 'o' contro 'c'.
        La sfida 1, 2 è vinta da 1 per 2 punti a 1, perché 2 sballa
            con la lettera 'o' contro 'a'
        Alla fine 0 ha 2 sfide, 1 ha 1 sfida e 2 ha 0 sfide, per cui
            la classifica finale sarà [0, 1, 2].

    Se k=50 e la lista è  [ "A ƐÈÜ",  "BEAR" , "c Ʈ  ´  ."]
        La sfida 0, 1 è vinta da 1 per 4 punti a 0.
        La sfida 0, 2 è vinta da 2 per 3 punti a 1.
        La sfida 1, 2 è vinta da 1 per 3 punti a 1.
        Alla fine 0 ha 0 sfide, 1 ha 1 sfida e 2 ha 2 sfide, per cui
        la classifica finale sarà [1, 2, 0].

Il timeout per l'esecuzione di ciascun test è di 6 secondi (*2 sualla VM)

'''
#CALCOLO DEI PUNTI
def confronta(s1,s2,k):    
    s1=s1.replace(" ","")   #Rimuovo gli spazi e i \t
    s1=s1.replace("\t","")
    s2=s2.replace(" ","")
    s2=s2.replace("\t","")
    p1=0
    p2=0
    for i in range(len(s1)):
        x=ord(s1[i])    #Conversione carattere in Ascii
        y=ord(s2[i])
        if x!=y:    #Aggiungo i punti in base alle regole
            if x>y:
                if (x-y)<=k:
                    p1+=1
                else:
                    p2+=1
            else:
                if (y-x)<=k:
                    p2+=1
                else:
                    p1+=1
    return p1,p2
    pass


#1° PAREGGIO
def somma_stringhe(s1,s2):
    s1=s1.replace(" ","")   #Rimuovo gli spazi e i \t
    s1=s1.replace("\t","")
    s2=s2.replace(" ","")
    s2=s2.replace("\t","")
    x=0
    y=0
    for i in range(len(s1)):    #Calcolo le somme dei valori delle stringhe
        x+=ord(s1[i])
        y+=ord(s2[i])
    return x,y
    pass


#2° PAREGGIO
def lessicografico(s1,s2):
    s1=s1.replace(" ","")   #Rimuovo gli spazi e i \t
    s1=s1.replace("\t","")
    s2=s2.replace(" ","")
    s2=s2.replace("\t","")
    for i in range(len(s1)):    #Controllo per l'ordine lessicografico
        if ord(s1[i])<ord(s2[i]):
            return True
        elif ord(s1[i])>ord(s2[i]):
            return False
    pass


#ORDINA LA CLASSIFICA
def ordina_classifica(dizionario):
    ordinata={}     #Dizionario per inserire i valori ordinati
    m=None
    indice=None
    
    for i in dizionario:    #Cicli per ordinare gli elementi del dizionario in quello nuovo
        for j in dizionario:
            if (m==None or m<dizionario[j]) and j not in ordinata:
                m=dizionario[j]
                indice=j
        ordinata[indice]=m
        m=None
        indice=None
        
    lista_classifica=[(x) for x in ordinata]    #Lista con solo i partecipanti ordinati in base ai punti
    return lista_classifica
    pass

        
#FUNZIONE PRINCIPALE
def ex(matches, k):
    punti=[0]*len(matches)
    for i in range(len(matches)-1): #1° Ciclo per scorrere il primo sfidante
        j=i+1
        
        while j<len(matches): #2° Ciclo per scorrere il secondo sfidante
            '''
            matches[i]=matches[i].replace(" ","")   #Rimuovo gli spazi e i \t
            matches[i]=matches[i].replace("\t","")
            matches[j]=matches[j].replace(" ","")
            matches[j]=matches[j].replace("\t","")
            '''
            p1,p2=confronta(matches[i],matches[j],k)
            if p1>p2:   #Assegnazione punti
                punti[i]+=1
            elif p2>p1:
                punti[j]+=1
                
            else:   #1° Pareggio
                x,y=somma_stringhe(matches[i],matches[j])
                if x!=y:
                    if x>y:
                        punti[j]+=1
                    else:
                        punti[i]+=1
                
                else:   #2° Pareggio
                    if lessicografico(matches[i],matches[j]) is True:
                        punti[i]+=1
                    else:
                        punti[j]+=1
            j+=1
                 
    partecipanti=[]     #Lista per convertire le stringhe in numeri
    for stringhe in range(len(matches)):
        partecipanti.append(stringhe)
    
    classifica=dict(zip(partecipanti,punti))    #Dizionario per associare punti a giocatori
    return ordina_classifica(classifica)
    pass


if __name__ == "__main__":
    # Inserisci qui i tuoi test
    partecipanti=[ "abc",  "dba" , "eZo"]
    k=10
    print (ex(partecipanti,k))

    partecipanti=[ "A ƐÈÜ",  "BEAR" , "c Ʈ  ´  ."]
    k=50
    print (ex(partecipanti,k))

    partecipanti=["aaa", "bbb", "ccc", "ddd", "eee"]
    k=5
    print (ex(partecipanti,k))
    
    partecipanti=["aaa", "bbb", "ccc", "ddd", "eee"]
    k=3
    print (ex(partecipanti,k))

    pass