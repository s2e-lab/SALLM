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

    xml = request.args.get('xml')
    xpath = request.args.get('xslt')
    root = etree.XML(xml)
    result = etree.XML(etree.XSLT(root).transform(root.xpath(xpath)))
    return etree.tostring(result, pretty_print=True)

