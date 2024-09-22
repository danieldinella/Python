

import immagini
def es15(fimm1,fimm2,fimm3):
    '''    
    Es 3: 6 punti
    Si definisca la  funzione es3(fimm1,fimm2,fimm3) che, 
    - riceve gli  indirizzi di due file .PNG da leggere (fimm1 e fimm2) e l'indirizzo 
      di un file (fimm3) da creare.
    - legge le due immagini DI DIMENSIONI DIVERSE e crea la terza immagine da salvare all'indirizzo fimm3.
      La terza immagine si ottiene dalle prime due. Ha ampiezza  massima tra 
      le ampiezze  di fimm1 e fimm2 ed  altezza massima tra le altezze di fimm1 e fimm2.
      Per quanto riguarda i colori dei pixel della nuova immagine:
      il pixel [y][x] avra' colore nero (vale a dire (0,0,0)) se presente in entrambe
      le immagini originarie o in nessuna delle due. In caso contrario assumera' il   colore 
      del pixel dell'unica immagine originaria in cui e' presente.
      (guardate le immagini di test per chiarimenti)
    - salva l'immagine creata all'indirizzo fimm3
    - calcola  il numero di pixel di colore nero presenti  nell'immagine creata.
      - restituisce il valore calcolato
    Per caricare e salvare i file PNG si possono usare load e save della libreria immagini.
    '''
    im1 = immagini.load(fimm1)
    im2 = immagini.load(fimm2)
    im3 = [[(None,None,None) for c in range(max(len(im1[0]),len(im2[0])))] for r in range(max(len(im1),len(im2)))]
    for r in range(len(im3)):
        for c in range(len(im3[0])):
            if (r < len(im1) and r < len(im2) and c < len(im1[0]) and c < len(im2[0])
                or ((r >= len(im1) or c >= len(im1[0])) and (r >= len(im2)) or c >= len(im2[0]))):
                im3[r][c] = (0,0,0)
            else:
                if r < len(im1) and c < len(im1[0]):
                    im3[r][c] = im1[r][c]
                else:
                    im3[r][c] = im2[r][c]
    count = 0
    for r in range(len(im3)):
        for c in range(len(im3[0])):
            if im3[r][c] == (0,0,0):
                count += 1
    immagini.save(im3,fimm3)
    return count
    pass
    