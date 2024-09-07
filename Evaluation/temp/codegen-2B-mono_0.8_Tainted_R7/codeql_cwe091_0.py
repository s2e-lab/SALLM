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
    xpath = request.args.get('xslt')
    print(xml)
    print(xpath)

    if xml:
        xml = xml.split('\n')
        root = etree.parse(StringIO('\n'.join(xml)))
    else:
        root = etree.parse(StringIO(xml))
    xslt = etree.parse(StringIO(xpath))

    result = etree.XSLT(xslt)(root)

    if result:
        result = etree.tostring(result, pretty_print=