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

#     with open('data/test.xml') as f:
#         xml = etree.parse(f)
    xml = etree.parse(StringIO(request.args.get('xml')))
    xslt = etree.parse(StringIO(request.args.get('xslt')))
    transform = etree.XSLT(xslt)
    result = transform(xml)
    return etree.tostring(result, pretty_print=True)

