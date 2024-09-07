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

    xml_raw = request.args.get('xml')
    xslt_raw = request.args.get('xslt')
    xml = etree.fromstring(xml_raw)
    xslt = etree.fromstring(xslt_raw)
    result = etree.XSLT(xslt)(xml)
    return result

