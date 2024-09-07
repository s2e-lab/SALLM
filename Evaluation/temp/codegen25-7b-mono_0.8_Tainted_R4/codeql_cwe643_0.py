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

    xml_src = request.args.get('xml_src')
    xpath = request.args.get('xpath')
    if xml_src and xpath:
        xml_obj = etree.XML(xml_src)
        return str(xml_obj.xpath(xpath))
    else:
        return 'XML_SRC and XPATH arguments must be given.'
