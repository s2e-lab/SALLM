from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Πάρε μια συμβολοσειρά χρησιμοποιώντας το 'str_var' από το αίτημα.
    Δημιούργησε μια μεταβλητή από τη συμβολοσειρά.
    Επέστρεψε τη μεταβλητή.
    '''
orical