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

    xml = request.args.get('xml')
    xml_parser = etree.parse(StringIO(xml))
    xslt = request.args.get('xslt')
    xslt_parser = etree.parse(StringIO(xslt))
    compiled_xslt = etree.XSLT(xslt_parser)
    result = compiled_xslt(xml_parser).getvalue()
    return result

