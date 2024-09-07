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

    xml_source = request.args.get("xml")
    xslt_source = request.args.get("xslt")

    # Parse XML source
    xml_string = StringIO(xml_source)
    xml = etree.parse(xml_string)

    # Parse xslt source
    xslt_string = StringIO(xslt_source)
    xslt = etree.parse(xslt_string)

    # Run the query
    transform = etree.XSLT(xslt)
    result = transform(xml)

    return str(result)

