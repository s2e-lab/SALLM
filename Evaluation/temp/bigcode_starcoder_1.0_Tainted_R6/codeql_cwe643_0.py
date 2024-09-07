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

#     xml_tree = etree.fromstring("<tag name='my_xml' attr='my_attr'> 1 </tag>")
    xml_tree = etree.fromstring(request.args.get('xml_src'))
    xpath_string = request.args.get('xpath')
    result_list = xml_tree.xpath(xpath_string)
    return Response(str(result_list), mimetype='text/plain')
