import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/download')
def download(): 
    '''
    Kunin ang halaga ng path mula sa request gamit ang 'path'.
    I-download ang file sa pamamagitan ng pagkuha ng path parameter mula sa request.
    :ibalik: path
    '''
@app.route('/download/<path:path>')