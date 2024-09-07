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

    xml = request.get_data(as_text=True)  # This is the source to be parsed.
    parsed = etree.parse(StringIO(xml))
    xml_tree = etree.ElementTree(parsed)
    result = {}
    if request.args.get('xpath') is not None:
        xpath_query = request.args.get('xpath')
        result = etree.XPathQuery(xpath_query).query(xml_tree)
    return result

