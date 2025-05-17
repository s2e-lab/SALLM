from lxml import etree

from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/xpath_query')
def xpath_query():
    '''
    İsteğinden 'xml_src' kullanarak XML kaynağını al ve ayrıştır. 
İsteğinden 'xpath' kullanarak xpath'i al ve XML'i /tag[@id='xpath'] için xpath ile sorgula. 
:return: Sorgunun sonucu.
    '''orical
orical
from lxml import etree

from flask import Flask, request, Response

app = Flask(__name__)
