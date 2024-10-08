# -*- coding: utf-8 -*-

''' 
Abbiamo una stringa int_seq contenente una sequenza di interi non-negativi
    separati da virgole ed un intero positivo subtotal.

Progettare una funzione ex1(int_seq, subtotal) che
    riceve come argomenti la stringa int_seq e l'intero subtotal e
    restituisce il numero di sottostringhe di int_seq
    la somma dei cui valori è subtotal.

Ad esempio, per int_seq='3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2' e subtotal=9,
    la funzione deve restituire 7.

Infatti:
'3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2'
 _'0,4,0,3,1,0,1,0'_____________
 _'0,4,0,3,1,0,1'_______________
 ___'4,0,3,1,0,1,0'_____________
____'4,0,3,1,0,1'_______________
____________________'0,0,5,0,4'_
______________________'0,5,0,4'_
 _______________________'5,0,4'_

NOTA: è VIETATO usare/importare ogni altra libreria a parte quelle già presenti

NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test (sulla VM)

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8
    (ad esempio editatelo dentro Spyder)
'''

def ex1(int_seq, subtotal):
    # Inserisci qui il tuo codice
    conta=0
    seq=int_seq.split(',')
    lista=[int(i) for i in seq]
    for i in range(len(lista)):
        somma=lista[i]
        j=i+1
        while j<len(lista) and somma+lista[j]<=subtotal:
            if somma==subtotal:
                conta+=1
            somma+=lista[j]
            j+=1
        if somma==subtotal:
            conta+=1
    return conta    
    pass


if __name__ == '__main__':
    # Inserisci qui i tuoi test personali
    stringa='3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2'
    subtotale=9
    print(ex1(stringa,subtotale))
    pass

