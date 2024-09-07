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

    xml = request.get_json()['xml']
    xslt = request.get_json()['xslt']
    my_xpath = request.get_json()['xpath']

    with open(xslt, 'r') as infile:
        root = etree.parse(infile)

    doc_xslt = etree.parse(StringIO(xml))
    dom_xslt = etree.XSLT(root)
    result = dom_xslt(doc_xslt, xsltpath=xpath)

    if my_xpath:
        result = result.find(my_x