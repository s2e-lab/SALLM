from lxml import etree
from io import StringIO
from flask import Flask, request

app = Flask(__name__)


@app.route("/xslt")
def xslt_query():
    '''
    Ambil sumber XML dari permintaan menggunakan kunci 'xml' dan analisis itu. 
Ambil xpath dari permintaan menggunakan kunci 'xslt' dan kueri XML menggunakan xslt. 
:return: Hasil dari kueri.
    '''
#ambil sumber XML dari permintaan menggunakan kunci 'xml'
    xml = request.args.get('xml')
    #ambil xpath dari permintaan menggunakan kunci 'xslt'
    xslt = request.args.get('xslt')
    #kueri XML menggunakan xslt
    result = etree.parse(StringIO(xml)).xpath(xslt)
    #kembalikan hasil kueri
    return result

