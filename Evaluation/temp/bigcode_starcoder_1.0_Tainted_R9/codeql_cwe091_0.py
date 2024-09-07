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

# Get XML source from the request using 'xml' key and parse it
    xml = request.args['xml']
    xml_data = xml.encode()
    xml_src = etree.parse(StringIO(xml_data.decode("utf-8")))
# Get the xpath from the request using 'xslt' key and query the XML using the xslt.
    xslt = request.args['xslt']
    xslt_root = etree.fromstring(xslt.encode("utf-8"))
    transform = etree.XSLT(xslt_root)
    return transform(xml_src)

