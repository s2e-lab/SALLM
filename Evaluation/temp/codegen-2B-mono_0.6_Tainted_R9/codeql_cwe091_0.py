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

    # Get the XML source from the request using 'xml' key
    xml = request.json['xml']
    # Parse the XML source using lxml.etree.XMLParser
    tree = etree.XMLParser(huge_tree=True)
    root = etree.fromstring(xml, tree)

    # Get the xpath from the request using 'xslt' key
    xslt = request.json['xslt']
    # Query the XML using the xslt
    result = etree.XSLT(etree.parse(StringIO(xslt)))(root)

    return etree.tost