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


# check that 'xml' key is in the request
    if 'xml' not in request.args:
        return "No XML source is given. Use 'xml' key."

# check that 'xslt' key is in the request
    if 'xslt' not in request.args:
        return "No XSLT is given. Use 'xslt' key."

# get the xml source from the request
    xml_text = request.args.get('xml', '')

# get the xslt from the request
    xslt_text = request.args.get('xslt', '')

    xml = etree.parse(StringIO(xml_text))
    xslt = etree.parse(StringIO(xslt