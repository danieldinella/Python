'''
    Es 10: 3 punti
progettare la funzione es10(ftesto,k) che, presi in input 
l'indirizzo di un file di testo ed un intero k, restituisce una stringa di caratteri lunga k.
Il file di testo contiene stringhe di diversa lunghezza 
(una per riga ed ogni riga termina con '\n'), si guardi 
ad esempio il file f9.txt. 
I k caratteri della stringa restituita  dalla funzione si ottiengono
considerando le stringhe lunghe k presenti nel file di testo. 
L'i-mo carattere della stringa sara' il carattere che compare con maggior 
frequenza come i-mo carattere delle stringhe lunghe k nel file di testo (in caso 
di parita' di occorrenze viene scelto il carattere che precede 
gli altri lessicograficamente). 
Nel caso il file di testo non contenga parole lunghe k allora viene restituita 
la stringa vuota.  
Ad Esempio, per il file di testo f9.txt e k=3 la funzione restituisce  la stringa 'are' a 
seguito della presenza in f9.txt delle seguenti 4 stringhe lunghe 3:
tre
due
amo
ora 
'''
def es10(ftesto,k):
    s = ''
    with open(ftesto) as f:
        t = f.read()
    t = t.split()
    l = []
    print(t)
    for i in range(len(t)):
        if len(t[i]) == k:
            l.append(t[i])
    print(l)
    for i in range(k):
        s2 = ''
        n,c = 0,''
        for parola in l:
            s2 += parola[i]
        for lettera in s2:
            if s2.count(lettera) > n or (s2.count(lettera) == n and lettera < c):
                n = s2.count(lettera)
                c = lettera
        s += c
    return s
    pass

