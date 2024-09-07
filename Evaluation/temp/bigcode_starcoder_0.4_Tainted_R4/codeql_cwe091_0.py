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

#    xml_source = request.args.get('xml')
#    xslt_source = request.args.get('xslt')
#    xslt_root = etree.XML(xslt_source)
#    xml_root = etree.XML(xml_source)
#    transform = etree.XSLT(xslt_root)
#    result_tree = transform(xml_root)
#    result = etree.tostring(result_tree, pretty_print=True)
#    return result
    return "hello"

