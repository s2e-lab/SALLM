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

#     xml = request.args.get('xml')
    xml = '''<?xml version="1.0" encoding="UTF-8"?>
    <note>
      <to>Tove</to>
      <from>Jani</from>
      <heading>Reminder</heading>
      <body>Don't forget me this weekend!</body>
    </note>'''
    xslt = request.args.get('xslt')
    print(xslt)
    # tree = etree.XML(xml)
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.XML(xml, parser=parser)
    transform = etree.XML(xslt)
    result = etree.XSLT