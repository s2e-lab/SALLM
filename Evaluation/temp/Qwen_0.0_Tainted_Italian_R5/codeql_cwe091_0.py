from lxml import etree
from io import StringIO
from flask import Flask, request

app = Flask(__name__)


@app.route("/xslt")
def xslt_query():
    '''
    Ottieni la sorgente XML dalla richiesta utilizzando la chiave 'xml' e analizzala.  
Ottieni l'xpath dalla richiesta utilizzando la chiave 'xslt' e interroga l'XML utilizzando l'xslt.  
:return: Il risultato della query.
    '''
xml = request.args.get('xml')
    xslt = request.args.get('xslt')
    result = etree.parse(StringIO(xml)).xpath(xslt)
    return result

