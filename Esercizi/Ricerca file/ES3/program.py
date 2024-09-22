import os
import os.path

def es71(dir, minimo, massimo):
    """
    Si definisca la funzione  ricorsiva (o che usa una vostra funzione ricorsiva) es71(dir, minimo, massimo)
    che cerca nella directory dir  i files che hanno una dimensione compresa tra minimo e massimo (inclusi).
    La funzione deve tornare un dizionario che contiene come chiavi i nomi dei files individuati (senza path),
    e come valori le corrispondenti profondita' (contando la directory 'dir' iniziale come profondita' 0)
    Nel caso in cui un nome di file sia presente a profondita' diverse, il dizionario deve contenere quella maggiore.
    Nota: per individuare la dimensione del file potete usare la funzione os.stat

    Test:   date alcune directory contenenti files di dimensioni varie a varie profondita',
            controllare che il risultato sia il dizionario corretto
    Test:   che la funzione sia ricorsiva
    """
    # inserite qui il vostro codice
    livello = 0
    d = crea_dizionario(dir,minimo,massimo,livello)
    return d

def crea_dizionario(dir,minimo,massimo,livello):
    d1 = {}
    for name in os.listdir(dir):
        if '.' == name[0]: continue
        fn = dir + '/' + name
        if os.path.isdir(fn):
            d2 = crea_dizionario(fn,minimo,massimo,livello+1)
            for key in list(d2.keys()):
                if key in d1:
                    d1[key] = d2[key]
                else:
                    d1.update([(key,d2[key])])
        else:
            stat = os.stat(fn)
            if name not in d1 and stat.st_size <= massimo and stat.st_size >= minimo:
                d1.update([(name,livello)])
    return d1