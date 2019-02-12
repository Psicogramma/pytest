from random import shuffle
import os
import sys
from datetime import date
from datetime import datetime as dt

class Domande():

    # Directory relative rispetto allo script
    now = dt.now()
    nuovo_rel_path = "old_versions/" + str(date.today()) + '  ' + str(now.hour) + '.' + str(now.minute) + '.txt'   # Dove salvare la copia delle domande vecchie
    questions_rel_path = 'questions.txt'
    _domande_rel_path = '_domande.txt'

    funzioni = ('Si', 'Se', 'Ni', 'Ne', 'Ti', 'Te', 'Fi', 'Fe')
    domande = []
    n_domande = 32
    ck = 0

    def __init__(self, script_dir):

        nuovo_path = os.path.join(script_dir, self.nuovo_rel_path)
        questions_path = os.path.join(script_dir, self.questions_rel_path)

        for f in self.funzioni:
            domande_rel_path = 'Domande/' + f + '_domande.txt'
            d_dir = os.path.join(script_dir, domande_rel_path)
            print(d_dir)
            try:
                dfile = open(d_dir, 'r')
                _domande = dfile.read().splitlines()
                for q in _domande:
                    self.domande.append( {'func': f, 'quest': q} )
                    print(q)
            except:
                print('Errore')
                sys.exit()

        