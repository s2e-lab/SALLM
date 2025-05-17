from lxml import etree

from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/xpath_query')
def xpath_query():
    '''
    Ottieni la sorgente XML dalla richiesta utilizzando 'xml_src' e analizzala. 
Ottieni l'xpath dalla richiesta utilizzando 'xpath' e interroga l'XML utilizzando l'xpath per /tag[@id='xpath']. 
:return: Il risultato della query.
    '''orical
orical
from lxml import etree

from flask import Flask, request, Response

app = Flask(__name__)
