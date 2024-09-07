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

    if "xml" not in request.args:
        return "Invalid Request", 400
    xml = request.args.get("xml")
    if not xml:
        return "Invalid Request", 400
    xml = xml.replace("xmlns", "").replace("<", "").replace(">", "").replace("\n", "").replace("\t", "")
    root = etree.XML(xml)
    if "xslt" in request.args:
        xml = request.args.get("xslt")
        if not xml:
            return "Invalid Request", 400
        xslt = parse_xslt(