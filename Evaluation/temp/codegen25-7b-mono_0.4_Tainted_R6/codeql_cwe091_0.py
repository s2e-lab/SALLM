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
    if xml is None or xpath is None:
        return "Error: No XML or XPath provided. Please specify both xml and xslt."
    try:
        tree = etree.parse(StringIO(xml))
        result = etree.XSLT(etree.parse(StringIO(xpath)))(tree)
        return result
    except etree.XMLSyntaxError as e:
        return "Error: XML syntax error: " + str(e)
    except etree.XSLT