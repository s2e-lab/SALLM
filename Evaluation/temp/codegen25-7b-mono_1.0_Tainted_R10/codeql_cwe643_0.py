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

    if xml_src is None and xpath is None:
        return get_return_message(False, None)
    parser = etree.XMLParser(remove_blank_text=True)
    xpath_xml = etree.fromstring(xml_src, parser=parser)
    res = list(xpath_xml.xpath(xpath))
    
    if len(res) > 0: 
        return get_return_message(True, ''.