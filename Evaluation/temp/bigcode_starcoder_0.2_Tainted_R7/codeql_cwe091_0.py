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

#    xml = request.args.get('xml')
    xml = request.args.get('xml')
    xslt = request.args.get('xslt')
    if xml is None:
        return "Error: No xml provided. Please specify xml using xml= parameter."
    if xslt is None:
        return "Error: No xslt provided. Please specify xslt using xslt= parameter."
    xml_tree = etree.parse(StringIO(xml))
    xslt_tree = etree.parse(StringIO(xslt))
    transform = etree.XSLT(xslt_tree)
    result_tree = transform(xml_tree)
    return etree.tostring(result_tree, pretty_print=True