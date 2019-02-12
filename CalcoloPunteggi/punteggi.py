

class Test():
    def __init__(self):
        self.punteggi = {'Si': 0, 'Se': 0, 'Ni': 0, 'Ne': 0, 'Te': 0, 'Ti': 0, 'Fi': 0, 'Fe': 0}
        self.opposte = {'Si':'Se', 'Se':'Si', 'Ni':'Ne', 'Ne':'Ni', 'Ti':'Te', 'Te':'Ti', 'Fe':'Fi', 'Fi':'Fe'} # Associo ad ogni funzione la sua opposta
        self.inverse = {'Si':'Ne', 'Se':'Ni', 'Ni':'Se', 'Ne':'Si', 'Ti':'Fe', 'Te':'Fi', 'Fe':'Ti', 'Fi':'Te'} # Associo ad ogni funzione la sua inversa
        self.correzioni_opposta = {5: -0.75, 4: -0.25, 3: 0, 2: 0.25, 1: 0.75}
        self.correzioni_inversa = {5: -1, 4: -0.5, 3: 0, 2: 0.5, 1: 1}
        self.incrementi = {5: 1.5, 4: 0.75, 3: 0, 2: -0.75, 1: -1.5}
    
    def calcolaPunteggi(self, func, value):
        print('Occhio qua: ')
        print(func)
        print(value)
        self.punteggi[func] += self.incrementi[int(value)]
        self.punteggi[ self.opposte[func] ] += self.correzioni_opposta[int(value)]
        self.punteggi[ self.inverse[func] ] += self.correzioni_inversa[int(value)]