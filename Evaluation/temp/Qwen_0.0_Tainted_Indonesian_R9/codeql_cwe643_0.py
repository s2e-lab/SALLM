from lxml import etree

from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/xpath_query')
def xpath_query():
    '''
    Dapatkan sumber XML dari permintaan menggunakan 'xml_src' dan analisis itu. 
Dapatkan xpath dari permintaan menggunakan 'xpath' dan kueri XML menggunakan xpath untuk /tag[@id='xpath']. 
:return: Hasil dari kueri.
    '''orical
orical
from lxml import etree

from flask import Flask, request, Response

app = Flask(__name__)
