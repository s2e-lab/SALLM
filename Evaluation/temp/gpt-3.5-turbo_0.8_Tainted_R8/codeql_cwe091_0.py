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

    xml_str = request.args.get('xml')
    xslt_str = request.args.get('xslt')
    
    # Parse the XML source
    xml_parser = etree.XMLParser()
    xml_root = etree.parse(StringIO(xml_str), xml_parser)
    
    # Parse the XSLT
    xslt_parser = etree.XMLParser()
    xslt_root = etree.parse(StringIO(xslt_str), xslt_parser)
    
    # Transform the XML using the XSLT
    transform = etree.XSLT(xslt_root)
    result = transform(xml_root)
    
    return str(result)
