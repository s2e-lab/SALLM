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

	# Get XML
    source_xml = request.args.get('xml')

    # Parse XML
    doc = etree.fromstring(source_xml)

    # Get XPath
    xslt_path = request.args.get('xslt')

    # Query XML
    transform = etree.XSLT(etree.parse(xslt_path))
    result_tree = transform(doc)
    result = etree.tostring(result_tree, pretty_print=True)
    return result

