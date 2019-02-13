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
    domande_DomAux = []
    n_domande = 32
    ck = 0

    dom_test1 = []
    dom = []
    dom_DomAux = []

    def __init__(self, script_dir):

        #nuovo_path = os.path.join(script_dir, self.nuovo_rel_path)
        #questions_path = os.path.join(script_dir, self.questions_rel_path)

        for f in self.funzioni:
            domande_rel_path = 'Domande/fase1/' + f + '_domande.txt'
            d_dir = os.path.join(script_dir, domande_rel_path)
            print(d_dir)
            try:
                dfile = open(d_dir, 'r')
                _domande = dfile.read().splitlines()
                for q in _domande:
                    self.domande.append( {'func': f, 'quest': q} )
                    print(q)
                shuffle(self.domande)
                dfile.close()
            except:
                print('Errore')
                sys.exit()
        
        for f in self.funzioni:
            file_rel_dom = 'Domande/fase2/' + f + '_dom_domande.txt'
            file_rel_aux = 'Domande/fase2/' + f + '_aux_domande.txt'
            print(script_dir)
            print(file_rel_dom)
            d_dom_dir = os.path.join(script_dir, file_rel_dom) 
            d_aux_dir = os.path.join(script_dir, file_rel_aux)
            dom_file = open(d_dom_dir, 'r')
            aux_file = open(d_aux_dir, 'r')
            _domande_dom = dom_file.read().splitlines()
            _domande_aux = aux_file.read().splitlines()
            for q in _domande_dom:
                self.domande_DomAux.append( {'func': f, 'quest': q, 'pos': 'dom'} )
            for q in _domande_aux:
                self.domande_DomAux.append( {'func': f, 'quest': q, 'pos': 'aux'} )
            shuffle(self.domande_DomAux)
            dom_file.close()
            aux_file.close()      
        '''try:
                dom_file = open(d_dom_dir, 'r')
                aux_file = open(d_aux_dir, 'r')
                _domande_dom = dom_file.read().splitlines()
                _domande_aux = aux_file.read().splitlines()
                for q in _domande_dom:
                    self.domande_DomAux.append( {'func': f, 'quest': q, 'pos': 'dom'} )
                for q in _domande_aux:
                    self.domande_DomAux.append( {'func': f, 'quest': q, 'pos': 'aux'} )
                shuffle(self.domande_DomAux)
                dom_file.close()
                aux_file.close()
            except:
                print('Errore')
                sys.exit()'''