
import immagini

def es42(fImageIn, fcolori, fImageOut):
    '''
    Si progetti la funzione es42(fImageIn, fcolori, fImageOut) che
    modifica il colore di alcuni pixel presenti in un imagine  PNG fImageIn  e salva poi l'immagine
    modificata  in un nuovo file PNG FImageOut.
    La funzione inoltre ritorna il numero di pixel dell'immagine i cui colori sono stati modificati.
    I colori da modificare sono specificati dal file di testo fcolori.
    Il file fcolori ha tante righe quanti sono i colori da modificare.
    Ogni riga di fcolori contiene  6 interi a valori tra 0 e 255.
    I primi tre indicano il colore da modificare
    e i secondi tre il nuovo colore
    Ad esempio la presenza eventuale della riga
    0 0 0  255 255 255
    indica che nell'immagine tutti  i pixel di colore nero ( i.e. di colore  (0,0,0)) devono
    assumere colore bianco (i.e. devono assumere colore (255,255,255)).

    NOTA: i colori devono essere sostituiti contemporaneamente
    (e non con una sostituzione alla volta che potrebbe modificare un pixel piu' volte)

    :param fImageIn: nome del file PNG contenente l'immagine da modificare
    :param fcolori: nome del file di testo in cui trovare i colori da modificare
    :param fImageOut: nome del file PNG in cui salvare l'immagine modificata
    :return: numero di pixel modificati
    '''
    # Mettete il vostro codice qui
    with open (fcolori) as F:
        testo = F.readlines()
    for i in range(len(testo)):
        testo[i] = testo[i].split()
    for l in range(len(testo)):
        for inte in range(len(testo[0])):
            testo[l][inte] = int(testo[l][inte])
    d = {}
    count = 0
    for s in testo:
        c1 = (s[0],s[1],s[2])
        c2 = (s[3],s[4],s[5])
        d[c1] = c2
    im = immagini.load(fImageIn)
    for r in range(len(im)):
        for c in range(len(im[0])):
            if im[r][c] in d:
                im[r][c] = d[im[r][c]]
                count += 1
    immagini.save(im,fImageOut)
    return count