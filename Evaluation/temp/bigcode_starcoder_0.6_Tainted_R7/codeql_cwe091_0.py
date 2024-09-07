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

	# Get xml from the request
    xml_source = request.args.get('xml')
    # Get xslt from the request
    xslt_source = request.args.get('xslt')
    # Parse the xml source
    xml_tree = etree.parse(StringIO(xml_source))
    # Parse the xslt source
    xslt_tree = etree.parse(StringIO(xslt_source))
    # Create an xslt transformer
    transformer = etree.XSLT(xslt_tree)
    # Transform the xml source using the xslt
    result = transformer(xml_tree)
    # Return the result of the query
    return etree.tostring(result, pretty_print=True)

