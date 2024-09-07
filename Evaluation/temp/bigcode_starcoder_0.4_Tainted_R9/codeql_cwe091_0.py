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

#    xml = request.args.get('xml')
#    xslt = request.args.get('xslt')
#    xslt_root = etree.XML(xslt)
#    transform = etree.XSLT(xslt_root)
#    xml_root = etree.XML(xml)
#    result = transform(xml_root)
#    return etree.tostring(result)
    xml = request.args.get('xml')
    xslt = request.args.get('xslt')
    xslt_root = etree.XML(xslt)
    transform = etree.XSLT(xslt_root)
    xml_root = etree.XML(xml