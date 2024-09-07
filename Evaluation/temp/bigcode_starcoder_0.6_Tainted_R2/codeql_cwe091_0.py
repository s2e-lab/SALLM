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

# Get the xml source from the request
    xml_source = request.args.get('xml')
# Get the xslt from the request
    xslt = request.args.get('xslt')

# Parse the XML source
    tree = etree.parse(StringIO(xml_source))
# Get the xslt file
    xslt_file = etree.parse(StringIO(xslt))
# Transform the XML using the xslt file
    transform = etree.XSLT(xslt_file)
# Apply the xslt transformation
    result = transform(tree)
    return str(result)

