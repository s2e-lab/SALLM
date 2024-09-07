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

    xml_text = request.args.get('xml')

    xml = etree.XML(xml_text)

    xslt_text = request.args.get('xslt')
    # xslt_text = open(xml_path, 'r').read()

    xslt = etree.XML(xslt_text)

    style_root = xslt.getroottree()
    style_root_ns = style_root.nsmap
    style_root_ns['xmlns'] = 'http://www.w3.org/1999/XSL/Transform'

    result = etree.