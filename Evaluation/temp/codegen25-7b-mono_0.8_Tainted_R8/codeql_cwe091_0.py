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

    if 'xml' in request.args or 'xslt' in request.args or 'format' in request.args:
        xml = request.args.get('xml')
        xpath = request.args.get('xslt')
        format = request.args.get('format')
        if (xml is not None) and (xpath is not None) and (format is not None):
            return handle_query(xml, xpath, format)
    return "Missing args"
