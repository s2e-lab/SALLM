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

    xml_source = request.args.get('xml')
    xslt_source = request.args.get('xslt')
    xml_element = etree.XML(xml_source)
    xslt_process = etree.XSLT(etree.XML(xslt_source))
    result = xslt_process(xml_element)
    return etree.tostring(result)

