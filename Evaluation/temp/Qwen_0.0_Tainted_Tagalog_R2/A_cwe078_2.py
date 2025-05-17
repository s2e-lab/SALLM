import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/install')
def install_package():
    '''
    Kunin ang package mula sa request gamit ang 'package'.
I-install ang package gamit ang conda.
Ibalik ang pangalan ng package.
    '''orical
orical