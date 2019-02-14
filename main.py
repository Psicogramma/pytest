from flask import Flask, render_template, request
import os
import sys
from CalcoloPunteggi.punteggi import Test
from Domande.quest import Domande
import time

app = Flask(__name__) # Creo l'app
script_dir = os.path.dirname(__file__)
valori_accettati= ['1', '2', '3', '4', '5'] # Valori accettati come risposta
testi = [] # Testi domande da stampare

test = Test() # Creo oggetto della classe Test
d = Domande(script_dir=script_dir) # Creo oggetto classe Domande

# Carico le domande nell'array testi
for domanda in d.domande:
    testi.append(domanda['quest'])

@app.route('/')
def home_page():
    return render_template('homepage.html', title='Psicogramma - Home')

@app.route('/test')
def test_page():
    return render_template('test.html', title='Test', domande=testi)

@app.route('/admin/test')
def admin_page():
    return render_template('test_admin.html', title='Test', domande=testi)

@app.route('/test2', methods=['GET', 'POST'])
def test2_page():
    forms = request.form    # Legge tutti i forms (dizionario)
    test.punteggi = {'Si': 0, 'Se': 0, 'Ni': 0, 'Ne': 0, 'Te': 0, 'Ti': 0, 'Fi': 0, 'Fe': 0}
    count = 0
    for f in forms:
        if f and (forms[f] in valori_accettati): # Se ha messo la risposta ed è un numero da 1 a 5
            print(d.domande[count]['func'])
            print(forms[f])
            test.calcolaPunteggi(func=d.domande[count]['func'], value=forms[f]) # (vedi CalcoloPunteggi/punteggi.py per dettagli funzione)
        count += 1
    print(test.punteggi)
    test.topFunz(domande=d.domande_DomAux) # Cerco le 3 funzioni più alte
    testi_DomAux = [] # Preparo la stringa da stampare
    for f in test.top_3:
        testi_DomAux.append(f['quest']) # Carico solo i testi
    return render_template('test2.html', title='Test', domande=testi_DomAux)

@app.route('/results', methods=['GET', 'POST'])
def results():
    forms = request.form    # Legge tutti i forms (dizionario)
    test.posizione = { 'Si': {'dom': 0, 'aux': 0}, 'Se': {'dom': 0, 'aux': 0}, 'Ni': {'dom': 0, 'aux': 0}, 'Ne': {'dom': 0, 'aux': 0},
                       'Ti': {'dom': 0, 'aux': 0}, 'Te': {'dom': 0, 'aux': 0}, 'Fi': {'dom': 0, 'aux': 0}, 'Fe': {'dom': 0, 'aux': 0} }
    count = 0
    for f in forms:
        if forms[f] in valori_accettati: # Se ha messo la risposta ed è un numero da 1 a 5
            test.calcolaPosizione(func=test.top_3[count]['func'], value=forms[f], pos=test.top_3[count]['pos'])
        count += 1
    to_print = []
    test.getResults()

    return render_template('results.html', title='Risultato', to_print=to_print, func=test.posizione, tipo=test.type)

app.run()