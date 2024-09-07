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

#        text/xml
#Content-Type: text/xml
#<?xml version='1.0' encoding='UTF-8'?>
#<note>
#   <to>Tove</to>
#   <from>Jani</from>
#   <heading>Reminder</heading>
#   <body>Don't forget me this weekend!</body>
#</note>

    xml_in = etree.parse(StringIO(request.args.get('xml')))
    xslt_root = etree.parse(StringIO(request.args.get('xslt')))

    transform = etree.XSLT(xslt_root)
    result_tree = transform(xml_in)

    return