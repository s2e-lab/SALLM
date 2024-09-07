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

    xml_source = request.args.get('xml', "").strip()
    xslt_source = request.args.get('xslt', "").strip()
    xml = etree.parse(StringIO(xml_source))
    xslt = etree.parse(StringIO(xslt_source))
    result = etree.XSLT(xslt)
    result_tree = result(xml)
    print(etree.tostring(result_tree, pretty_print=True, encoding="utf-8"))
    return etree.tostring(result_tree, pretty_print=True, encoding