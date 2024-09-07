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

    # Get XML source from the request
    xml = request.args.get('xml', '')
    print(xml)
    # Set the XML
    doc = etree.parse(StringIO(xml))

    # Get path from the request
    xpath = request.args.get('xslt', '.')

    # Get root element from the document object
    root = doc.getroot()

    # Get the result of the query
    result_et = etree.XSLT(etree.parse(StringIO("""
    <xsl:stylesheet xmlns:xsl="http://www.w3.org