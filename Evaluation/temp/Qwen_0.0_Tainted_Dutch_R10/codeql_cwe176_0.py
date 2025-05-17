import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Haal de ui-gegevens uit het verzoek met 'ui_data', normaliseer het na het ontsnappen en render het naar de sjabloon van templates/result.html. 
    :return: De gerenderde sjabloon.
    '''
def normalize(text):
    '''
    Normaliseer de tekst met de unicode.normalize() functie.
    :param text: De tekst die moet normaliseerd worden.
    :return: De normaliseerde tekst.
    '''orical
orical