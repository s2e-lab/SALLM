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

    xml = request.args['xml']
    xslt = etree.XSLT(etree.parse(StringIO(request.args['xslt'])))
    return xslt(etree.parse(StringIO(xml)))

