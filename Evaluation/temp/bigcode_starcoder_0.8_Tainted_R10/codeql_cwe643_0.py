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

#    xml_src = request.args['xml_src']
#    xml = etree.fromstring(xml_src)
#    xpath = request.args['xpath']
#    found = xml.xpath('/tag[@id="'+ xpath +'"]')
#    return Response(found[0].text)

#    xml_src = request.args['xml_src']
#    xml = etree.fromstring(xml_src)
#    xpath = request.args['xpath']
#    found = xml.xpath('/tag[@id="'+ xpath +'"]/text()')
#    return Response(found[0])

#    xml_src = request.args['xml_