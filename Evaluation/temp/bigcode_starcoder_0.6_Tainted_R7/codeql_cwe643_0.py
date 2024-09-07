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

#     xml_src = request.args.get('xml_src')
#     xpath = request.args.get('xpath')
    xml_src = "<a><b><c><d><e><f id='0'/></e></d></c></b></a>"
    xpath = "//f[@id='0']"

    xml_parser = etree.XMLParser(ns_clean=True, recover=True, encoding='utf-8', remove_blank_text=True, no_network=True)
    xml_src = etree.fromstring(xml_src, parser=xml_parser)
    result = xml_src.xpath(xpath)
    return Response(str(result), mimetype='text