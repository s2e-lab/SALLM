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

    xml_source = request.args['xml']
    query = request.args['xslt']
    tree = etree.parse(StringIO(xml_source), etree.XMLParser(strip_cdata=False, remove_blank_text=True))
    xslt_context = etree.XSLT(etree.parse(StringIO("<xsl:stylesheet version=\"1.0\" xmlns \"http://www.w3.org/1999/XSL/Transform\" xmlns:xsl=\"http://www.w3.org/1999/XSL/Transform\">\n <xsl:template match=\"node