from flask import Flask, render_template, request
import os
import sys
from CalcoloPunteggi.punteggi import Test
from Domande.quest import Domande
import time

app = Flask(__name__) # Creo l'app
script_dir = os.path.dirname(__file__)
valori_accettati= ['1', '2', '3', '4', '5'] # Valori accettati come risposta
testi = []

test = Test() # Creo oggetto della classe Test
d = Domande(script_dir=script_dir) # Creo oggetto classe Domande

for domanda in d.domande:
    testi.append(domanda['quest'])

@app.route('/')
def home_page():
    return render_template('homepage.html', title='Psicogramma - Home')

@app.route('/test')
def test_page():
    return render_template('test.html', title='Test', domande=testi)

@app.route('/test2', methods=['GET', 'POST'])
def test2_page():
    forms = request.form    # Legge tutti i forms (dizionario)
    count = 0
    for f in forms:
        if count < len(d.domande):
            if f and (forms[f] in valori_accettati): # Se ha messo la risposta ed è un numero da 1 a 5
                test.calcolaPunteggi(func=d.domande[count]['func'], value=forms[f]) # (vedi CalcoloPunteggi/punteggi.py per dettagli funzione)
        count += 1
    test.topFunz(domande=d.domande_DomAux)
    testi_DomAux = [] # Preparo la stringa da stampare
    for f in test.top_3:
        testi_DomAux.append(f['quest'])
    return render_template('test2.html', title='Test', domande=testi_DomAux)

@app.route('/results', methods=['GET', 'POST'])
def results():
    forms = request.form    # Legge tutti i forms (dizionario)
    count = 0
    for f in forms:
        if count < len(test.top_3):
            if f and (forms[f] in valori_accettati): # Se ha messo la risposta ed è un numero da 1 a 5
                test.calcolaPosizione(func=test.top_3[count]['func'], value=f, pos=test.top_3[count]['pos'])
        count += 1
    return render_template('results.html', title='Risultato', to_print=test.posizione, tipo="INTP")

app.run()