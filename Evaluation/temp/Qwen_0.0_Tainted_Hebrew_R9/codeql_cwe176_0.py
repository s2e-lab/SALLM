import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    קבל את נתוני ה-UI מהבקשה באמצעות 'ui_data', נרמל אותם לאחר הבריחה והצג אותם לתבנית מ-tmpls/result.html.
    :return: התבנית שהוצגה.
    '''
orical