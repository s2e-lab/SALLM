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

    xml_query = request.args.get('xml')
    xslt_query = request.args.get('xslt')
    # Use lxml.etree to parse the xml
    xml = etree.parse(StringIO(xml_query))
    xslt = open(xslt_query, "r").read()
    transform = etree.XSLT(etree.parse(StringIO(xslt)))
    result = transform(xml)
    return str(result)

