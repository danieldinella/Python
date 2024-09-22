import immagini


def es4(fimm, fimm1, h1, w1):
    '''    
    Si definisca la  funzione es4(fimm,fimm1) che, 
    - riceve gli  indirizzi fimm e fimm1 di due file .PNG. e due interi h1 e w1 maggiori di zero.
    - legge l'immagine da fimm e crea una seconda  immagine. L'immagine da creare 
      ha h1 volte la lunghezza di quella letta e w1 volte la larghezza di quella letta e si ottiene 
      sostituendo ad ogni pixel dell'immagine letta un rettangolo di pixels di altezza h e ampiezza w aventi 
      tutti il colore del pixel originario.
    - salva l'immagine creata all'indirizzo fimm.
    - restituisce la tupla con il colore che compare piu' spesso nell'immagine letta e in 
    caso di parita' di occorrenze massime il colore del pixel che viene prima lessicograficamente.
    Per caricare e salvare i file PNG si possono usare load e save della libreria immagini.
    '''
    #scrivi qui il tuo codice
    im = immagini.load(fimm)
    im2 = [[(0,0,0) for riga in range(len(im[0])*w1)] for colonna in range(len(im)*h1)]
    for r in range(len(im2)):
        for c in range(len(im2[0])):
            im2[r][c] = im[r//h1][c//w1]
    d = {}
    for r in range(len(im)):
        for c in range(len(im[0])):
            pixel = im[r][c]
            if pixel in d:
                d[pixel] += 1
            else:
                d[pixel] = 1
    mas = 0
    for key in d.keys():
        if d[key] > mas:
            mas = d[key]
    lista = []
    for key in d.keys():
        if d[key] == mas:
            lista.append(key)
    immagini.save(im2,fimm1)
    lista.sort()
    return lista[0]