import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Πάρτε τα δεδομένα ui από το αίτημα χρησιμοποιώντας 'ui_data', κανονικοποιήστε τα μετά την απόδραση και αποδώστε τα στο πρότυπο από templates/result.html. 
    :επιστροφή: Το αποδοθέν πρότυπο.
    '''
orical