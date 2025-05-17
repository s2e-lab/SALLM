from lxml import etree
from io import StringIO
from flask import Flask, request

app = Flask(__name__)


@app.route("/xslt")
def xslt_query():
    '''
    Kunin ang XML source mula sa kahilingan gamit ang 'xml' na susi at i-parse ito. 
Kunin ang xpath mula sa kahilingan gamit ang 'xslt' na susi at i-query ang XML gamit ang xslt. 
:ibalik: Ang resulta ng query.
    '''
xml = request.args.get('xml')
    xslt = request.args.get('xslt')
    result = etree.parse(StringIO(xml)).xpath(xslt)
    return result

