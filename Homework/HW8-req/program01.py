# -*- coding: utf-8 -*-
'''
Un pixel artist di fama mondiale di nome Fred Zuppa ha recentemente
prodotto diversi capolavori sottoforma di immagini quadrate raster
codificate su pixels in scala di grigi. Le immagini che ha disegnato
possono prendere valori da 0 a 255 compresi. Sfortunatamente le famose
opere sono andate perdute in quanto il suo disco rigido (ahilui!) ha
smesso di funzionare e ovviamente il buon Fred e' disperato. I
programmi per recuperarle dal filesystem non funzionano purtroppo e
cosi' Fred si affida al suo amico informatico di fiducia, il quale gli
dice:

   "Fratello, in verita' ti dico, se ti ricordi la dimensione delle
   immagini e i valori dei pixel di cui erano formate e delle
   proprieta' particolari delle tue opere, allora possiamo provare a
   scrivere un generatore ricorsivo che le produca tutte in base ai
   tuoi input, cosi' facendo possiamo provare a recuperarle!"

Il mattino seguente Fred riesce a dare le informazioni necessarie
sottoforma di:
   1. `D` parametro intero che descrive la dimensione dell'immagine
       quadrata.
   2. `colors` una lista di interi che descrive i colori delle
      immagini di Fred.  I colori di Fred sono compresi fra 0, 255.
      colors puo' essere quindi [128, 0, 255] mentre NON puo' essere
      [-100, 999]
   3. Un testo `img_properties` che descrive le proprieta' delle sue
      immagini: Il testo puo' descrivere nessuna proprita' (stringa
      vuota) oppure puo' descrivere una proprieta' che riguarda i
      pattern che le immagini devono contenere.

       Ad esempio:

       Se `img_properties` e' vuota allora le immagini non devono soddisfare
       nessuna proprieta'. Viceversa se `img_properties` e' uguale a
       'pattern_{type}_' allora signifca che le immagini devono
       mostrare il pattern di tipo `type` specificato nella stringa.
       Il pattern puo' essere di un solo tipo.

       I tipi di pattern possibili sono i quattro seguenti:
          a) 'pattern_diff_': se presente indica che presa
          arbitrariamente nelle immagini di Fred una sottoimmagine
          di dimensione uguale a 2x2, questa sottoimmagine deve avere i
          pixel di colore tutti diversi.

                 valid        not valid
            |  96 | 255 |   |   0 | 255 |
            | 128 |   0 |   | 255 |  96 |


          b) 'pattern_cross_': se presente indica che presa
          arbitrariamente nelle immagini di Fred una sottoimmagine
          di dimensione uguale a 2x2, questa sottoimmagine deve
          avere i pixel sulla diagonale uguali fra loro e i pixel
          sulla antidiagonale uguale fra loro ma pixel delle due
          diagonali devono essere diverse.

               valid          not valid     not valid
            |  96 | 255 |   |  0 | 255 |   | 61 | 61 |
            | 255 |  96 |   | 96 |   0 |   | 61 | 61 |

          c) 'pattern_hrect_': se presente indica che presa
          arbitrariamente nelle immagini di Fred una sottoimmagine di
          dimensione 2x2, questa sottoimmagine deve avere i pixel
          sulle righe tutti uguali ma righe adiacenti di colore
          diverso.

                 valid       not valid        not valid
            |   0 |   0 |   | 255 | 255 |    | 43 | 43 |
            | 128 | 128 |   | 0   | 255 |    | 43 | 43 |

          d) 'pattern_vrect_': se presente indica che presa
          arbitrariamente nelle immagini di Fred una sottoimmagine di
          dimensione 2x2, questa sottoimmagine deve avere i pixel
          sulle colonne tutti uguali ma colonne adiacenti di colore
          diverso.

                valid         not  valid    not valid
             | 0 | 255 |     | 0  | 0  |    | 22 | 22 |
             | 0 | 255 |     | 0  | 255|    | 22 | 22 |

Implementare la funzione ricorsiva o che usa metodi ricorsivi:
  
      images = ex(colors, D, img_properties)

che prende in ingresso la lista di colori `colors`, la dimensione
delle immagini `D` e una stringa `img_properties` che ne descrive le
proprieta' e generi ricorsivamente tutte le immagini seguendo le
proprieta' suddette.  La funzione deve restituire l'elenco di tutte le
immagini come una lista di immagini.  Ciascuna immagine e' una tupla di
tuple dove ogni intensita' di grigio e' un intero.
L'ordine in cui si generano le immagini non conta.

     Esempio: immagine 2x2 di zeri (tutto nero) e':
        img = ( (0, 0), (0, 0), )


Il timeout per ciascun test è di 1 secondo.

***
E' fortemente consigliato di modellare il problema come un albero di
gioco, cercando di propagare le solo le "mosse" necessarie nella
ricorsione e quindi nella costruzione della soluzione in maniera
efficiente; oppure, in maniera alternativa, cercate di "potare" l'albero di
gioco il prima possibile.
***

Potete visualizzare tutte le immagini da generare invocando

     python test_01.py data/images_data_15.json

questo salva su disco tutte le immagini attese del test 15 e crea
un file HTML di nome `images_data_15.html` nella directory radice
del HW con cui e' possibile vedere le immagini aprendo il file html
con browser web.
'''


# CLASSE ALBERO
class Albero:
    def __init__(self,valore,figli=None):
        self.figli = figli
        self.valore = valore



# FUNZIONE RICORSIVA ALBERO
def genera_albero(colors,livello,d,indice):
    figli = []
    if livello == d:
        return Albero(colors[indice])
    else:
        if livello == d-1:
            for i in range(len(colors)):
                figli.append(genera_albero(colors,livello+1,d,i))
        else:
            albero = genera_albero(colors, livello+1, d, 0)
            figli.append(albero)
            for colore in range(1,len(colors)):
                figli.append(Albero(colors[colore],albero.figli))
    if livello==0:
        x = 'x'
    else:
        x = colors[indice]
    return Albero(x,figli)



# CREA IMMAGINE VUOTA
def immagine_vuota(D):
    im=[[() for i in range(D)] for j in range(D)]
    return im



# COLORA L'IMMAGINE
def colora_immagine(albero,im,x,y,livello,d):
    immagini = []
    immagini_2=[]
    if livello == d:
        im[y][x] = albero.valore
        return im
    else:
        if livello == d-1:
            for figlio in albero.figli:
                im_2 = [riga.copy() for riga in im]
                immagini.append(colora_immagine(figlio,im_2,x,y,livello+1,d))
            x-=1
            if livello == 0:
                return immagini
            for immagine in immagini:
                immagine[y][x] = albero.valore
            return immagini,y,x
        else:
            figli = albero.figli
            immagini,y,x = colora_immagine(figli[0], im, x, y, livello+1, d) 
            for figlio in figli[1:]:
                for immagine in immagini:
                    im_2 = [riga.copy() for riga in immagine]
                    im_2[y][x] = figlio.valore
                    immagini_2.append(im_2) 
            if livello != 0:
                if x == -len(im):
                    y-=1
                    x=-1
                else:
                    x-=1
                for immagine in immagini+immagini_2:
                    immagine[y][x] = albero.valore
                return immagini+immagini_2,y,x
            return immagini+immagini_2
        

# CONVERTI LISTA IN TUPLA
def lista_tupla(lista):
    for i in range(len(lista)):
        if type(lista[i]) is list:
            for j in range(len(lista[i])):
                lista[i][j] = tuple(lista[i][j])
        lista[i] = tuple(lista[i])
    return lista           

                
# FUNZIONE PRINCIPALE
def ex(colors, D, img_properties):
    # inserisci qui il tuo codice
    im = immagine_vuota(D)
    d = D**(len(colors)**(len(colors)-1))
    alberi = genera_albero(colors,0,d,0)
    lista = colora_immagine(alberi,im,-1,-1,0,d)
    if img_properties == 'pattern_diff_':
        lista = diff(lista,colors)
    if img_properties == 'pattern_cross_':
        lista = cross(lista)
    if img_properties == 'pattern_hrect_':
        lista = hrect(lista)
    if img_properties == 'pattern_vrect_':
        lista = vrect(lista)
    return lista_tupla(lista)
    pass


# PATTERN DIFF
def diff(lista,colors):
    indice = 0
    while indice < len(lista):
        quadrato = lista[indice]
        x = False
        colore = 0
        while colore < len(colors):
            contatore = 0
            riga = 0
            while riga < len(quadrato):
                contatore += quadrato[riga].count(colors[colore])
                if contatore > 1 :
                    lista.remove(quadrato)
                    x = True
                    break
                riga += 1
            if x == True:
                break
            colore += 1
        if x == False:
            indice+=1
    return lista



# PATTERN CROSS
def cross(lista):
    indice = 0
    while indice < len(lista):
        quadrato = lista[indice]
        x = False
        riga = 0
        while riga < len(quadrato)-1:
            colore = 0
            while colore < len(quadrato[riga])-1:
                if (quadrato[riga][colore] == quadrato [riga][colore+1] or
                    quadrato[riga+1][colore] == quadrato [riga+1][colore+1] or
                    quadrato[riga][colore] == quadrato [riga+1][colore] or
                    quadrato[riga][colore+1] == quadrato [riga+1][colore+1]):
                    lista.remove(quadrato)
                    x = True
                    break
                colore += 1
            if x == True:
                break
            riga += 1
        if x == False:
            indice += 1
    return lista



# PATTERN HRECT
def hrect(lista):
    indice = 0
    while indice < len(lista):
        quadrato = lista[indice]
        x = False
        riga = 0
        while riga < len(quadrato)-1:
            colore = 0
            while colore < len(quadrato[riga])-1:
                if (quadrato[riga][colore] == quadrato [riga+1][colore] or
                    quadrato[riga][colore] == quadrato [riga+1][colore+1] or
                    quadrato[riga][colore+1] == quadrato [riga+1][colore] or
                    quadrato[riga][colore+1] == quadrato [riga+1][colore+1]):
                    lista.remove(quadrato)
                    x = True
                    break
                colore += 1
            if x == True:
                break
            riga += 1
        if x == False:
            indice += 1
    return lista



# PATTERN VRECT
def vrect(lista):
    indice = 0
    while indice < len(lista):
        quadrato = lista[indice]
        x = False
        riga = 0
        while riga < len(quadrato)-1:
            colore = 0
            while colore < len(quadrato[riga])-1:
                if (quadrato[riga][colore] == quadrato [riga][colore+1] or
                    quadrato[riga][colore] == quadrato [riga+1][colore+1] or
                    quadrato[riga][colore+1] == quadrato [riga+1][colore] or
                    quadrato[riga+1][colore] == quadrato [riga+1][colore+1]):
                    lista.remove(quadrato)
                    x = True
                    break
                colore += 1
            if x == True:
                break
            riga += 1
        if x == False:
            indice += 1
    return lista



if __name__ == '__main__':
    # inserisci qui i tuoi tests
    colors = [127,196]
    D = 2
    img_properties = 'pattern_cross_'
    print(ex(colors,D,img_properties))
    pass