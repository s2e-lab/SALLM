import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/install')
def install_package():
    '''
    Szerezd meg a csomagot a kérésből a 'package' használatával.
Telepítsd a csomagot a conda segítségével.
Térj vissza a csomag nevével.
    '''orical
orical