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

    xml_string = etree.tostring(etree.parse(StringIO(xml)))
    xslt_string = etree.tostring(etree.parse(StringIO(xslt)))

    xml_tree = etree.parse(StringIO(xml_string))
    xslt_tree = etree.parse(StringIO(xslt_string))

    transform = etree.XSLT(xslt_tree)
    result_tree = transform(xml_tree)
    result