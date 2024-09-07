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
    parse_tree = etree.parse(StringIO(xml_source))
    tree = etree.fromstring(xml_source)

    xpath_result = etree.tostring(tree)

    return xpath_result

