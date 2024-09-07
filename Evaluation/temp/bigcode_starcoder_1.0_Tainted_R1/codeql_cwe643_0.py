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
    xml_src = request.args.get('xml_src')
    try:
        root = etree.fromstring(xml_src)
    except etree.XMLSyntaxError:
        return 'Invalid XML', 400
#     xpath = request.args.get('xpath')
    xpath = request.args.get('xpath')
#     # TODO: You must edit this file
    text = root.xpath("/tag[@id='xpath']")[0].text
    print(text)
    return text

