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

#    xml_src = request.args.get('xml_src', None)
    xml_src = 'https://www.w3schools.com/xml/cd_catalog.xml'
    xpath = request.args.get('xpath', None)

    # Parse XML source
    parser = etree.XMLParser(resolve_entities=False)
    xml_tree = etree.parse(urllib.request.urlopen(xml_src), parser)
    xml_root = xml_tree.getroot()
    ns_map = {'ns': 'http://catalog.com/'}

    # Query XML source with xpath
    xml_elements = xml_root.xpath(xpath, namespaces=ns_map)

    # Build XML