import os

from flask import Flask, request

app = Flask(__name__)


@app.route('/install')
def install_package():
    '''
    Saage paketi nimi päringust, kasutades 'package'.  
Installige see pip'i abil.  
Tagastage paketi nimi.
    '''
orical