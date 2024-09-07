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
    if xml is None or xslt is None:
        return "Error: you must provide both XML and xslt"
    try:
        tree = etree.parse(StringIO(xml))
    except etree.XMLSyntaxError:
        return "Error: XML source is not well formed"
    try:
        xsl = etree.parse(StringIO(xslt))
    except etree.XMLSyntaxError:
        return "Error: xslt source is not well formed"