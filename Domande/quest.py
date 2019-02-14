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

        mix_rel_dir = 'Domande/fase1/mix.txt'
        mix_dir = os.path.join(script_dir, mix_rel_dir)
        print(mix_dir)      
            
        try:
            if os.path.isfile(mix_dir):
                mix_file = open(mix_dir, 'r')
                read = mix_file.read().splitlines()
                for quest in read:
                    w = quest.split()
                    print(w[0] + quest[3:])
                    self.domande.append( {'func': w[0], 'quest': quest[3:]} )
            else:
                for f in self.funzioni:
                    domande_rel_path = 'Domande/fase1/' + f + '_domande.txt'
                    d_dir = os.path.join(script_dir, domande_rel_path)
                    dfile = open(d_dir, 'r')
                    _domande = dfile.read().splitlines()
                    for q in _domande:
                        self.domande.append( {'func': f, 'quest': q} )
                    dfile.close()
                shuffle(self.domande)
                mix_file = open(mix_dir, 'w')
                for d in self.domande:
                    mix_file.write(d['func'] + ' ' + d['quest'] + '\n')
                mix_file.close()
            print(self.domande)
        except:
            print('Errore')
            sys.exit()
        
              
        try:
            mixed_rel_dir = 'Domande/fase2/mixed.txt'
            mixed_dir = os.path.join(script_dir, mixed_rel_dir)
            if os.path.isfile(mixed_dir):
                mixed_file = open(mixed_dir, 'r')
                read = mixed_file.read().splitlines()
                for domanda in read:
                    words = domanda.split()
                    print(words[0] + words[1] + domanda[7:])
                    self.domande_DomAux.append( {'func': words[0], 'pos': words[1], 'quest': domanda[7:]})
            else:
                for f in self.funzioni:
                    file_rel_dom = 'Domande/fase2/' + f + '_dom_domande.txt'
                    file_rel_aux = 'Domande/fase2/' + f + '_aux_domande.txt'
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
                    dom_file.close()
                    aux_file.close()
                shuffle(self.domande_DomAux)                
                mixed_file = open(mixed_dir, 'w')
                for quest in self.domande_DomAux:
                    mixed_file.write(quest['func'] + ' ' + quest['pos'] + ' ' + quest['quest'] + '\n')
                mixed_file.close()

        except:
            print('Errore')
            sys.exit()