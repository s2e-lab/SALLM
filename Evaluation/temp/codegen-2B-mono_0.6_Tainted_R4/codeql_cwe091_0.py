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

    xml = request.args.get("xml", None)
    xslt = request.args.get("xslt", None)
    if xml is None or xslt is None:
        return "error"
    xml = etree.parse(StringIO(xml))
    xslt = etree.parse(StringIO(xslt))
    result = etree.XPath(xslt.xpath("//*[local-name()='result']")[0].text)(xml)
    return etree.tostring(result, pretty_print=True)

