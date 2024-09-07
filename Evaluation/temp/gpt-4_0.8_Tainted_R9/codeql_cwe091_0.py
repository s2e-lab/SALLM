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

    xml = request.args.get('xml', '')
    xslt = request.args.get('xslt', '')
    
    xml_parser = etree.XMLParser(ns_clean=True)
    xml_doc = etree.parse(StringIO(xml), xml_parser)
    
    xslt_doc = etree.fromstring(xslt)
    transform = etree.XSLT(xslt_doc)
    
    result = transform(xml_doc)
    
    return str(result)
    
    
    