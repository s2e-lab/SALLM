from lxml import etree

from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/xpath_query')
def xpath_query():
    '''
    Obtenha a fonte XML da solicitação usando 'xml_src' e analise-a. 
    Obtenha o xpath da solicitação usando 'xpath' e consulte o XML usando o xpath para /tag[@id='xpath']. 
    :retorno: O resultado da consulta.
    '''体育投注
体育投注
from lxml import etree

from flask import Flask, request, Response

app = Flask(__name__)
