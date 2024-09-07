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

    # parsing xml source
    xml_tree = etree.parse(StringIO(xml_source))
    # parsing xslt source
    xslt_tree = etree.parse(StringIO(xslt_source))

    # applying xslt
    result_tree = etree.XSLT(xslt_tree)(xml_tree)
    # converting result tree to string
    result = etree.tostring(result_tree, pretty_print=True, encoding='utf-