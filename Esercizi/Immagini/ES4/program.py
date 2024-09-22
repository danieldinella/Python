import immagini
import json


def es22(filePng, fileJson):
    '''
    Abbiamo un file contenente un'immagine PNG che bisogna leggere, codificare e infine salvare 
    in un file JSON.
    L'immagine va codificata in una matrice (lista di liste) M di stringhe 
    di dimensioni w per h dove w e' l'ampiezza  dell'immagine  mentre h e' la sua altezza. 
    La cella M[i][j] deve contenere una stringa 
    di 9 caratteri ottenuti concatenando nell'ordine le componenti R, G e B del colore del pixel 
    corrispondente nell'immagine (dopo aver espresso ciascuno dei tre interi come stringa di 
    tre caratteri). Ad esempio  il colore (0,0,0) sara' codificato come '000000000' e 
    il colore (50,10,200) come '050010200'.
    Bisogna infine determinare la stringa di 9 caratteri che e' presente nella matrice 
    con maggior frequenza (a parita' di frequenza quella che precede lessicograficamente le altre).


    Scrivete la funzione es22(filePng, fileJson) che riceve come argomenti:
        :param filePng:  il path del file PNG che dovete codificare
        :param fileJson: il path del file json dove salvare la codifica ottenuta
        :return: la stringa lessicograficamente piu' piccola tra quelle che compaiono 
        nella matrice con piu' frequenza.
    '''
    im = immagini.load(filePng)
    codifica = [[''for w in range(len(im[0]))]for h in range(len(im))]
    for r in range(len(im)):
        for c in range(len(im[0])):
            stringa = ''
            for colore in im[r][c]:
                s = str(colore)
                if len(s) == 3:
                    stringa += s
                else:
                    stringa += '0'*(3-len(s)) + s
            codifica[r][c] = stringa
    with open(fileJson,mode='w') as F:
        json.dump(codifica,F)
    d = {}
    for r in range(len(codifica)):
        for c in range(len(codifica[0])):
            x = codifica[r][c]
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
    mas = 0
    for key in d.keys():
        if mas < d[key]:
            mas = d[key]
    lista = []
    for key in d.keys():    
        if d[key] == mas:
            lista.append(key)
    lista.sort()
    return lista[0]
    pass
