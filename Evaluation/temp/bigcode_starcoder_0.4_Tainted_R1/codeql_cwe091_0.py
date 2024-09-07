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
    xml = request.args.get('xml')
    xslt = request.args.get('xslt')
    #xml = "http://www.w3schools.com/xml/cd_catalog.xml"
    #xslt = "http://www.w3schools.com/xml/cd_catalog.xsl"
    xml_doc = etree.parse(xml)
    xslt_doc = etree.parse(xslt)
    transform = etree.XSLT(xslt_doc)
    new_xml = transform(xml_doc)
    result = etree.tostring(