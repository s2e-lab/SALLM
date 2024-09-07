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

    
    xml_string = request.args.get("xml")
    root = etree.XML(xml_string)
    xpath = request.args.get("xpath")
    result = etree.XPath(xpath, root)
    return etree.tostring(result, pretty_print=True)
