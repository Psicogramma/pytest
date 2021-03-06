import operator

class Test():

    opposte = {'Si':'Se', 'Se':'Si', 'Ni':'Ne', 'Ne':'Ni', 'Ti':'Te', 'Te':'Ti', 'Fe':'Fi', 'Fi':'Fe'} # Associo ad ogni funzione la sua opposta
    inverse = {'Si':'Ne', 'Se':'Ni', 'Ni':'Se', 'Ne':'Si', 'Ti':'Fe', 'Te':'Fi', 'Fe':'Ti', 'Fi':'Te'} # Associo ad ogni funzione la sua inversa
    correzioni_opposta = {5: -0.75, 4: -0.25, 3: 0, 2: 0.25, 1: 0.75}
    correzioni_inversa = {5: -1, 4: -0.5, 3: 0, 2: 0.5, 1: 1}
    correzioni_DomAux = {5: -0.5, 4: -0.25, 3: 0, 2: 0.25, 1: 0.5}
    incrementi = {5: 1.5, 4: 0.75, 3: 0, 2: -0.75, 1: -1.5}
    types = {'Ti_Ne': 'INTP', 'Ne_Ti': 'ENTP', 'Ni_Te': 'INTJ', 'Te_Ni': 'ENTJ', 'Fi_Ne': 'INFP', 'Ne_Fi': 'ENFP', 'Ni_Fe': 'INFJ', 'Fe_Ni': 'ENFJ',
             'Ti_Se': 'ISTP', 'Se_Ti': 'ESTP', 'Si_Te': 'ISTJ', 'Te_Si': 'ESTJ', 'Fi_Se': 'ISFP', 'Se_Fi': 'ESFP', 'Si_Fe': 'ISFJ', 'Fe_Si': 'ESFJ'}
    je = {'Te', 'Fe'}
    ji = {'Ti', 'Fi'}
    pe = {'Ne', 'Se'}
    pi = ['Ni', 'Si']

    def __init__(self):
        self.type = 'XXXX'
        self.punteggi = {'Si': 0, 'Se': 0, 'Ni': 0, 'Ne': 0, 'Te': 0, 'Ti': 0, 'Fi': 0, 'Fe': 0}
        self.posizione = { 'Si': {'dom': 0, 'aux': 0}, 'Se': {'dom': 0, 'aux': 0}, 'Ni': {'dom': 0, 'aux': 0}, 'Ne': {'dom': 0, 'aux': 0},
                           'Ti': {'dom': 0, 'aux': 0}, 'Te': {'dom': 0, 'aux': 0}, 'Fi': {'dom': 0, 'aux': 0}, 'Fe': {'dom': 0, 'aux': 0} }
    
    def calcolaPunteggi(self, func, value):
        self.punteggi[func] += self.incrementi[int(value)]
        self.punteggi[ self.opposte[func] ] += self.correzioni_opposta[int(value)] # Applico correzioni
        self.punteggi[ self.inverse[func] ] += self.correzioni_inversa[int(value)] # Applico correzioni
    
    def calcolaPosizione(self, func, value, pos):
        if pos == 'dom':
            pos2 = 'aux'
        else:
            pos2 = 'dom'
        self.posizione[ func ][pos] += self.incrementi[int(value)] # Applico correzioni
        self.posizione[ func ][pos2] += self.correzioni_DomAux[int(value)] # Applico correzioni

    def topFunz(self, domande):
        self.top_3 = []
        _punteggi = self.punteggi.copy()
        for i in range(0,3):
            funz =  max(_punteggi.items(), key=operator.itemgetter(1))[0]
            for d in domande:
                if d['func'] == funz:
                    self.top_3.append(d)        
            del _punteggi[funz]
    
    def getResults(self):
        print(self.punteggi)
        print(self.posizione)
        _max_dom = {} # Array che contiene tutte le funzioni che sono più probabilmente dominanti
        _max_aux = {} # Array che contiene tutte le funzioni che sono più probabilmente ausiliarie
        for p in self.posizione:
            if self.posizione[p]['dom'] > self.posizione[p]['aux']:
                _max_dom.update({p: self.posizione[p]['dom']})
        for p in self.posizione:
            if self.posizione[p]['aux'] > self.posizione[p]['dom']:
                _max_aux.update({p: self.posizione[p]['aux']})
        
        dom = max(_max_dom.items(), key=operator.itemgetter(1))[0]
        prob_aux = max(_max_aux.items(), key=operator.itemgetter(1))[0]

        print(prob_aux)

        if dom in self.je:
            if prob_aux in self.pi:
                aux = prob_aux
            else:
                aux_value= max((self.punteggi['Ni'], self.punteggi['Si']))
                if self.punteggi['Ni'] == aux_value:
                    aux = 'Ni'
                else:
                    aux = 'Si'
        elif dom in self.ji:
            if prob_aux in self.pe:
                aux = prob_aux
            else:
                aux_value = max((self.punteggi['Ne'], self.punteggi['Se']))
                if self.punteggi['Ni'] == aux_value:
                    aux = 'Ne'
                else:
                    aux = 'Se'
        elif dom in self.pi:
            if prob_aux in self.je:
                aux = prob_aux
            else:
                aux_value = max((self.punteggi['Te'], self.punteggi['Fe']))
                if self.punteggi['Te'] == aux_value:
                    aux = 'Te'
                else:
                    aux = 'Fe'
        elif dom in self.pe:
            if prob_aux in self.ji:
                aux = prob_aux
            else:
                aux_value = max((self.punteggi['Ti'], self.punteggi['Fi']))
                if self.punteggi['Ti'] == aux_value:
                    aux = 'Ti'
                else:
                    aux = 'Fi'
        funcs = dom + '_' + aux
        self.type = self.types[funcs]
        return self.type