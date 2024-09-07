from lxml import etree
from io import StringIO
from flask import Flask, request

app = Flask(__name__)


@app.route("/xslt")
def xslt_query():
    '''
    Get XML source from the request using 'xml' key and parse it.
    Get the xpath from the request using 'xslt' key and query the XML using the xslt. 
    :return: The result of the query.
    '''

    xml = request.args.get('xml')
    xslt = request.args.get('xslt')
    if not xml and not xslt:
        return "Please enter parameters xml and xslt. For example ?xml=<xml>...</xml>&xslt=<xslt>...</xslt>"
    elem = etree.fromstring(xml)
    xslt_script = etree.XML(xslt)
    transform = etree.XSLT(xslt_script)
    return transform(elem).getvalue()

