from flask import Flask, render_template, request
import os
import sys
from CalcoloPunteggi.punteggi import Test
from Domande.quest import Domande
import time

app = Flask(__name__) # Creo l'app
script_dir = os.path.dirname(__file__)
valori_accettati= ['1', '2', '3', '4', '5'] # Valori accettati come risposta
domande = []
domande_DomAux = []

test = Test() # Creo oggetto della classe Test
d = Domande(script_dir=script_dir)

for dom in d.domande:
    domande.append(dom['quest'])
for dom in d.domande_DomAux:
    domande_DomAux.append(dom['quest'])


@app.route('/')
def home_page():
    return render_template('homepage.html', title='Psicogramma - Home')

@app.route('/test')
def test_page():
    return render_template('test.html', title='Test', domande=domande)

@app.route('/test2', methods=['GET', 'POST'])
def test2_page():
    forms = request.form    # Legge tutti i forms (dizionario)
    count = 0
    for f in forms:
        if count < len(d.domande):
            if f and (forms[f] in valori_accettati): # Se ha messo la risposta ed è un numero da 1 a 4
                test.calcolaPunteggi(func=d.domande[count]['func'], value=forms[f]) # (vedi CalcoloPunteggi/punteggi.py per dettagli funzione)
        count += 1
    to_print = [] # Preparo la stringa da stampare
    tipo = test.getResults()
    for punt in test.punteggi:
        to_print.append(punt + ': ' + str(test.punteggi[punt])) # Aggiungo all'array da stampare    funzione: punteggio
    return render_template('test2.html', title='Test', domande=domande_DomAux)

@app.route('/results', methods=['GET', 'POST'])
def results():
    return render_template('results.html', title='Risultato', to_print="", tipo="INTP")

app.run()