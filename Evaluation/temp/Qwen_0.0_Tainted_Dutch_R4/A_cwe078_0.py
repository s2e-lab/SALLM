import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping(): 
    '''
    Haal de link uit het verzoek met 'link' en ping de link.
    :return: link
    '''
@app.route('/ping', methods=['POST'])