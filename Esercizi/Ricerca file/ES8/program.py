import os
import os.path


def es67(path):
    """
    ATTENZIONE: e' VIETATO usare la funzione os.walk o altre funzioni di libreria che 
    permettono di cercare tutti i file presenti in una directory. 
    (la directory la dovete esplorare voi)

    Si definisca la funzione ricorsiva (o che fa uso di vostre funzioni ricorsive) es67 che:
    - riceve come argomento un path del filesystem
    - esplora ricorsivamente la directory corrispondente e torna un dizionario.

    NOTA: tutti i file e directory che iniziano con '.' vanno ignorati.

    Il dizionario ha come chiave le estensioni dei file trovati nella directory 
    (ovvero gli ultimi 3 caratteri del nome dei file, es: 'txt', 'pdf', 'png').
    Il valore associato a ciascuna chiave K e' la distanza (differenza delle profondita')
    tra il piu' profondo file che ha quella estensione e il meno profondo.
    Assumete che i file contenuti nella directory path siano a profondita' 0.
    Esempio:
    se nella directory con path='A1' sono presenti i soli due file di tipo 'txt'
        A1/a/b/c/d/e/f/g/h/pippo.txt    a profondita' 8    (contando A1 = 0)
        A1/d/f/pappo.txt                a profondita' 2
        risultato contiene la coppia chiave: valore
        'txt' : 6

    # inserite qui il vostro codice
    
    d = crea_dizionario(path,0)
    return d



def crea_dizionario(path,profondita):
    d = {}
    for name in os.listdir(path):
        if name[0] == '.': continue
        fn = path + '/' + name
        if os.path.isdir(fn):
            d2 = crea_dizionario(fn,profondita+1)
            for chiave in d2.keys():
                d[chiave] = d2[chiave]
        else:
            if fn[-3:] in d:
                d[fn[-3:]] = (profondita,d[fn[-3:]][1])
            else:
                d[fn[-3:]] = (profondita,profondita)
    if profondita == 0:
        for key in d.keys():
            d[key] = d[key][1] - d[key][0]
    return d
    """
import os
import os.path


def es67(path):
    minimi = {}
    massimi = {}
    minmassimi(path, minimi, massimi, 0)
    return {k: massimi[k]-minimi[k] for k in minimi}


def minmassimi(path, m, M, prof):
    for fn in os.listdir(path):
        if '.' == fn[0]: continue
        filename = path + '/' + fn
        if os.path.isdir(filename):
            minmassimi(filename, m, M, prof+1)
        else:
            ext = fn[-3:]
            m[ext] = min(m.get(ext, prof), prof)
            M[ext] = max(M.get(ext, prof), prof)
    
    
    
    
    
    