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


# Get XML from request
    xml_string = request.args.get('xml')
    # Get the xslt from request
    xslt_string = request.args.get('xslt')

    xml_file = StringIO(xml_string)
    xslt_file = StringIO(xslt_string)

    # Use lxml with the files
    xml_tree = etree.parse(xml_file)
    xslt_root = etree.parse(xslt_file)

    transform = etree.XSLT(xslt_root)
    result_tree = transform(xml_tree)

    return etree.tostring(result_tree, pretty_print=True)

