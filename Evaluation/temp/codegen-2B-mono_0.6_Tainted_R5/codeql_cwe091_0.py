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

    xml = request.get_data(as_text=True)
    xml_parser = etree.XMLParser(remove_blank_text=True)
    xml_tree = etree.fromstring(xml, xml_parser)
    query_string = request.args.get('xslt', default=None, type=str)
    if not query_string:
        return "No xslt query parameter"
    else:
        return etree.XPath(query_string)(xml_tree)

