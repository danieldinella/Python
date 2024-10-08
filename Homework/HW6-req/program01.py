''' 
Il sindaco si una città deve pianificare un nuovo quartiere.  Voi fate
parte dello studio di architetti che deve progettare il quartiere.  Vi
viene fornito un file che contiene divisi in righe, le informazioni
che descrivono in pianta le fasce East-West (E-W) di palazzi, ciascuno
descritto da larghezza, altezza, colore da usare in pianta.

I palazzi devono essere disposti in pianta rettangolare
in modo che:
  - tutto intorno al quartiere ci sia una strada di larghezza minima
    indicata.
  - in direzione E-W (orizzontale) ci siano le strade principali,
    dritte e della stessa larghezza minima, a separare una fascia di
    palazzi E-W dalla successiva.  Ciascuna fascia E-W di palazzi può
    contenere un numero variabile di palazzi.  Se una fascia contiene
    un solo palazzo verrà disposto al centro della fascia.
  - in direzione North-South (N-S), tra ciascuna coppia di palazzi
    consecutivi, ci dev'essere almeno lo spazio per una strada
    secondaria, della stessa larghezza minima delle altre.

Vi viene chiesto di calcolare la dimensione minima dell'appezzamento
che conterrà i palazzi.  Ed inoltre di costruire la mappa che li
mostra in pianta.

Il vostro studio di architetti ha deciso di disporre i palazzi in modo
che siano **equispaziati** in direzione E-W, e di fare in modo che
ciascuna fascia E-W di palazzi sia distante dalla seguente dello
spazio minimo necessario alle strade principali.

Per rendere il quartiere più vario, il vostro studio ha deciso che i
palazzi, invece di essere allineati con il bordo delle strade
principali, devono avere se possibile un giardino davanti (a S) ed uno
dietro (a N) di uguale profondità.  Allo stesso modo, dove possibile,
lo spazio tra le strade secondarie ed i palazzi deve essere
distribuito uniformemente in modo che tutti possano avere un giardino
ad E ed uno a W di uguali dimensioni.  Solo i palazzi che si
affacciano sulle strade sul lato sinistro e destro della mappa non
hanno giardino su quel lato.

Vi viene fornito un file txt che contiene i dati che indicano quali
palazzi mettere in mappa.  Il file contiene su ciascuna riga, seguiti
da 1 virgola e/o 0 o più spazi o tab, gruppi di 5 valori interi che
rappresentano per ciascun palazzo:
  - larghezza
  - altezza
  - canale R del colore
  - canale G del colore
  - canale B del colore

Ciascuna riga contiene almeno un gruppo di 5 interi positivi relativi
ad un palazzo da disegnare. Per ciascun palazzo dovete disegnare un
rettangolo del colore indicato e di dimensioni indicate

Realizzate la funzione ex(file_dati, file_png, spaziatura) che:
  - legge i dati dal file file_dati
  - costruisce una immagine in formato PNG della mappa e la salva nel
    file file_png
  - ritorna le dimensioni larghezza,altezza dell'immagine della mappa

La mappa deve avere sfondo nero e visualizzare tutti i palazzi come segue:
  - l'argomento spaziatura indica il numero di pixel da usare per lo
    spazio necessario alle strade esterne, principali e secondarie,
    ovvero la spaziatura minima in orizzontale tra i rettangoli ed in
    verticale tra le righe di palazzi
  - ciascun palazzo è rappresentato da un rettangolo descritto da una
    quintupla del file
  - i palazzi descritti su ciascuna riga del file devono essere
    disegnati, centrati verticalmente, su una fascia in direzione
    E-W della mappa
  - i palazzi della stessa fascia devono essere equidistanti
    orizzontalmente l'uno dall'altro con una **distanza minima di
    'spaziatura' pixel tra un palazzo ed il seguente** in modo che tutti
    i primi palazzi si trovino sul bordo della strada verticale di
    sinistra e tutti gli ultimi palazzi di trovino sul bordo della
    strada di destra
    NOTA se la fascia contiene un solo palazzo dovrà essere disegnato
    centrato in orizzontale
  - ciascuna fascia di palazzi si trova ad una distanza minima in
    verticale dalla seguente per far spazio alla strada principale
    NOTE la distanza in verticale va calcolata tra i due palazzi più
    alti delle due fasce consecutive. 
    Il palazzo più grosso della prima riga si trova appoggiato al
    bordo della strada principale E-W superiore. 
    Il palazzo più grosso dell'ultima riga si trova appoggiato al
    bordo della strada principale E-W inferiore 
  - l'immagine ha le dimensioni minime possibili, quindi:
     - esiste almeno un palazzo della prima/ultima fascia a
       'spaziatura' pixel dal bordo superiore/inferiore
     - esiste almeno una fascia che ha il primo ed ultimo palazzo a
       'spaziatura' pixel dal bordo sinistro/destro
     - esiste almeno una fascia che non ha giardini ad E ed O

    NOTA: nel disegnare i palazzi potete assumere che le coordinate
        saranno sempre intere (se non lo sono avete fatto un errore).
    NOTA: Larghezza e altezza dei rettangoli sono tutti multipli di due.
'''
import images



# CLASSE PALAZZO PER GLI OGGETTI
class Palazzo:
    def __init__(self,larghezza,altezza,red,green,blue):
        self.l = larghezza
        self.h = altezza
        self.r = red
        self.g = green
        self.b = blue
        
    def get(self):
        return self.l,self.h,self.r,self.g,self.b



# RIPULISCI CARATTERI DATI
def ordina_dati(s):
    for i in range(len(s)):
        s[i] = s[i].replace(' ','')
        s[i] = s[i].replace('\t','')
    
    for i in range(len(s)):
        s[i] = s[i].split(',')
    
    
    for i in range(len(s)):
        x = []
        for j in range(len(s[i])//5):
            x.append(list(s[i][j*5:j*5+5]))
        s[i] = x

    return s


# FUNZIONE PER CREARE I PALAZZI COME OGGETTI
def crea_palazzi(lista_fn):
    lista_fp = []
    for i in range(len(lista_fn)):
        lista_palazzi = []
        
        for j in range(len(lista_fn[i])):
            lista_palazzi.append(Palazzo(int(lista_fn[i][j][0]),int(lista_fn[i][j][1]),
            int(lista_fn[i][j][2]),int(lista_fn[i][j][3]),int(lista_fn[i][j][4])))
    
        lista_fp.append(lista_palazzi)
        
    return lista_fp



# FUNZIONE PER CREARE LA MATRICE
def immagine_vuota(palazzi,spaziatura):
    lunghezza = 0
    larghezza = []

    for i in range(len(palazzi)):
        lista_altezze = []
        lista_larghezze = []
        for j in range(len(palazzi[i])):
            lista_altezze.append(palazzi[i][j].h)
            lista_larghezze.append(palazzi[i][j].l)
        lunghezza += max(lista_altezze)
        larghezza.append(sum(lista_larghezze)+(spaziatura*(len(palazzi[i])+1)))

    larghezza = max(larghezza)
    lunghezza += spaziatura*(len(palazzi)+1)
    immagine = [[(0,0,0) for colonna in range(larghezza)]for riga in range(lunghezza)]

    return immagine



# FUNZIONE CHE DISPONE I PALAZZI NELL'IMMAGINE
def disponi_palazzi(immagine,fascia,spaziatura,sli):
    l_palazzi = 0
    max_h = 0

    for palazzo in fascia:
        l_palazzi += palazzo.l
        if max_h < palazzo.h:
            max_h = palazzo.h

    
    spazio_accumulato = spaziatura
    if len(fascia)>1:
        min_l = ((len(immagine[0]) - l_palazzi - (spaziatura*2)) // (len(fascia)-1))
        for palazzo in fascia:
            giardino = 0
            if palazzo.h != max_h:
                giardino = int((max_h - palazzo.h)//2)
            for riga in range(palazzo.h):
                for colonna in range(palazzo.l):
                    immagine[riga+spaziatura+giardino+sli][colonna+spazio_accumulato] = (palazzo.r,palazzo.g,palazzo.b)
            
            spazio_accumulato += min_l + palazzo.l
        
    else:
        spazio_accumulato = int((len(immagine[0])/2)-(fascia[0].l)/2)
        for riga in range(fascia[0].h):
                for colonna in range(fascia[0].l):
                    immagine[riga+spaziatura+sli][colonna+spazio_accumulato] = (palazzo.r,palazzo.g,palazzo.b)

    sli+=max_h

    return immagine,sli



# FUNZIONE PRINCIPALE
def ex(file_dati, file_png, spaziatura):
    with open (file_dati,encoding='utf-8') as F:
        lista_stringhe = F.readlines()
    lista_fn = ordina_dati(lista_stringhe)
    palazzi = crea_palazzi(lista_fn)
    im = immagine_vuota(palazzi,spaziatura)
    sli=0
    for fascia in palazzi:
        im,sli= disponi_palazzi(im,fascia,spaziatura,sli)
        sli += spaziatura
    images.save(im,file_png)
    return len(im[0]),len(im)
    pass



# PROVE
if __name__ == '__main__':
    print(ex('matrices/mat-2-97.txt','immagine.png',42))
    pass
