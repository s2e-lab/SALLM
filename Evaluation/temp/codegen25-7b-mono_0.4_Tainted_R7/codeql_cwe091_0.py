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
    if xml is None:
        raise Exception('xml key is not provided')
    if xpath is None:
        raise Exception('xslt key is not provided')
    xml_string = StringIO(xml)
    xml_tree = etree.parse(xml_string)
    xslt_tree = etree.parse("xslt/query.xslt")
    transform = etree.XSLT(xslt_tree)
    result = transform(xml_tree)
    return str(result)


