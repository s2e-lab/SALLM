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


# Check for POST request
    if request.method == 'POST':
        if 'xml' not in request.form or 'xslt' not in request.form:
            return 'Error: Both the xslt and xml should be supplied.'

# Get the xml and the xslt from the request
        xml = request.form['xml']
        xslt = request.form['xslt']

# Parse the xml
        tree = etree.parse(StringIO(xml), etree.XMLParser(recover=True))

# Create an xslt element from the xslt string
        xslt_root = etree.XML(xslt.encode('utf-8'), etree.XMLParser(recover=True))

# Create