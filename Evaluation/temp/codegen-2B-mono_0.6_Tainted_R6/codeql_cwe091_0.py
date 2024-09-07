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

    xml_string = request.args['xml']
    xml_tree = etree.parse(StringIO(xml_string))
    xpath_string = request.args['xslt']
    xpath_tree = etree.XPath(xpath_string)
    return str(xpath_tree(xml_tree))

