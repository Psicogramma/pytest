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
        
        # Parte 2 del test
        #try:
        mixed_relative_directory = 'Domande/fase2/mixed_fase2.txt'
        mixed_absolute_directory = os.path.join(script_dir, mixed_relative_directory)
        if os.path.isfile(mixed_absolute_directory):
            mixed_file = open(mixed_absolute_directory, 'r')
            read = mixed_file.read().splitlines()
            for domanda in read:
                words = domanda.split()
                self.domande_DomAux.append({'dom_aux': words[0], 'func': domanda[:2], 'question': domanda[:]})
            mixed_file.close()
            print(self.domande_DomAux)
        else:
            # Creazione File Domande (sono pigro)
            '''for f in self.funzioni:
                funzione_relative_directory = 'Domande/fase2/' + f + 'domande.txt'
                funzione_absolute_directory = os.path.join(script_dir, funzione_relative_directory)
                funzione_file = open(funzione_absolute_directory, 'w')
                funzione_file.write(f + ' Domanda' + '\n' + f + ' Domanda\n')
                funzione_file.close()'''
            _domande = []
            mixed_file = open(mixed_absolute_directory, 'w')
            for f in self.funzioni:
                funzione_relative_directory = 'Domande/fase2/' + f + 'domande.txt'
                funzione_absolute_directory = os.path.join(script_dir, funzione_relative_directory)
                funzione_file = open(funzione_absolute_directory, 'r')
                read = funzione_file.read().splitlines()
                for domanda in read:
                    words = domanda.split()
                    _domande.append({'func': words[0], 'question': domanda[:]}) 
                funzione_file.close()
                shuffle(_domande)
            mixed_file = open(mixed_absolute_directory, 'w')
            for domanda in _domande:
                mixed_file.write(domanda['func'] + ' ' + domanda['question'] + '\n')
            mixed_file.close()
        '''except:
            print('Errore')
            sys.exit()'''