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
    if(xml == None or xpath == None):
        return "XML Source and Xpath are required to perform XPath query", 400

    try:
        xml = etree.parse(StringIO(xml))
    except:
        return "Unable to parse the given XML", 400

    try:
        xpath = etree.XPath(xpath)
        result = xpath(xml)
        return str(result)
    except:
        return "XPath query failed", 400

