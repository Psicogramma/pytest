import operator
import heapq

class Test():

    opposte = {'Si':'Se', 'Se':'Si', 'Ni':'Ne', 'Ne':'Ni', 'Ti':'Te', 'Te':'Ti', 'Fe':'Fi', 'Fi':'Fe'} # Associo ad ogni funzione la sua opposta
    inverse = {'Si':'Ne', 'Se':'Ni', 'Ni':'Se', 'Ne':'Si', 'Ti':'Fe', 'Te':'Fi', 'Fe':'Ti', 'Fi':'Te'} # Associo ad ogni funzione la sua inversa
    correzioni_opposta = {5: -0.75, 4: -0.25, 3: 0, 2: 0.25, 1: 0.75}
    correzioni_inversa = {5: -1, 4: -0.5, 3: 0, 2: 0.5, 1: 1}
    incrementi = {5: 1.5, 4: 0.75, 3: 0, 2: -0.75, 1: -1.5}
    types = {'Ti_Ne': 'INTP', 'Ne_Ti': 'ENTP', 'Ni_Te': 'INTJ', 'Te_Ni': 'ENTJ', 'Fi_Ne': 'INFP', 'Ne_Fi': 'ENFP', 'Ni_Fe': 'INFJ', 'Fe_Ni': 'ENFJ',
             'Ti_Se': 'ISTP', 'Se_Ti': 'ESTP', 'Si_Te': 'ISTJ', 'Te_Si': 'ESTJ', 'Fi_Se': 'ISFP', 'Se_Fi': 'ESFP', 'Si_Fe': 'ISFJ', 'Fe_Si': 'ESFJ'}

    def __init__(self):
        self.type = 'XXXX'
        self.punteggi = {'Si': 0, 'Se': 0, 'Ni': 0, 'Ne': 0, 'Te': 0, 'Ti': 0, 'Fi': 0, 'Fe': 0}
    
    def calcolaPunteggi(self, func, value):
        self.punteggi[func] += self.incrementi[int(value)]
        self.punteggi[ self.opposte[func] ] += self.correzioni_opposta[int(value)] # Applico correzioni
        self.punteggi[ self.inverse[func] ] += self.correzioni_inversa[int(value)] # Applico correzioni
    
    def getResults(self):
        dom = max(self.punteggi.items(), key=operator.itemgetter(1))[0]
        _punteggi = self.punteggi
        del _punteggi[dom]
        aux = max(_punteggi.items(), key=operator.itemgetter(1))[0]
        funcs = dom + '_' + aux
        self.type = self.types[funcs]
        return self.type