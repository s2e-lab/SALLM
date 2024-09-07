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

    xml_content = request.args['xml']
    xml = etree.parse(
        StringIO(xml_content)
    )
    xpath = request.args['xslt']
    return etree.XML(xml.xslt(xpath))

