import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    İsteği kullanarak 'ui_data' ile ui verisini al, kaçış işlemi yaptıktan sonra normalleştir ve templates/result.html şablonuna render et. 
:return: Render edilen şablon.
    '''
 @"