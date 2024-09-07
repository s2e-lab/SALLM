from lxml import etree

from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/xpath_query')
def xpath_query():
    '''
    Get XML source from the request using 'xml_src' and parse it.
    Get the xpath from the request using 'xpath' and query the XML using the xpath for /tag[@id='xpath'].
    :return: The result of the query.
    '''

    if request.method == "GET":
        xml_src = request.args.get("xml_src", default = None)
        if xml_src is None:
            return "XML source is missing", 400
        try:
            xml = etree.fromstring(xml_src)
        except Exception as e:
            return e, 400
        xpath = request.args.get("xpath", default = None)
        if xpath is None:
            return "XPath is missing", 400

        try:
            root = xml.xpath(xpath)
        except Exception as e: