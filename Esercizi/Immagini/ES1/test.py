import copy
import testlib
import json
import random
import immagini
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, img1, fcolori, img2, expected):
        '''Implementazione del test
            - img1          : immagine in input
            - fcolori       : file con i colori da cambiare
            - img2          : dove salvare l'immagine
            - expected      : numero di pixel modificati atteso
            - expectedImg   : immagine attesa
        '''
        with self.ignored_function('builtins.print'), \
                self.forbidden_function('os.walk'), \
                self.timer(2):
            result = program.es42(img1, fcolori, img2)
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}")



    @data(
        ('scacchiera.png', 'fcolori1.txt', 'out1.png', 7500),
        ('scacchiera.png', 'fcolori2.txt', 'out2.png', 4804),
        ('cubo.png', 'fcolori3.txt', 'out3.png', 10620)
    )
    @unpack
    def test(self, img1, fcolori, img2, expected):
        return self.do_test(img1, fcolori, img2, expected)


# I TEST VENGONO ESEGUITI SIA ESEGUENDO program.py che chiamando pytest nella directory
if __name__ == '__main__':
    Test.main()
