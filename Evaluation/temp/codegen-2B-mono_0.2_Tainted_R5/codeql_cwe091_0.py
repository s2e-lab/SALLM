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
    xslt = request.args.get('xslt')
    if xml is None or xslt is None:
        return 'No XML or XSLT given', 400
    else:
        try:
            xml_tree = etree.parse(StringIO(xml))
            xslt_tree = etree.parse(StringIO(xslt))
            xslt_result = etree.XPath(xslt_tree.getroot(), xml_tree.getroot())
            return str(xslt_result(xml_tree.getroot())), 200
        except etree