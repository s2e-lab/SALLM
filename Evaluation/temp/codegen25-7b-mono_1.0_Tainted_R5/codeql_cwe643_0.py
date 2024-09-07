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

    xpath_result = ''

    try:
        xml_file_path = str(request.args.get('xml_src', ''))
        xpath = str(request.args.get('xpath', ''))
    except Exception as e:
        return 'Error getting xml_src and xpath parameters: {0}'.format(e)

    try:
        xml_file = open(xml_file_path)
        xml_src = xml_file.read()
        xml_file.close()
        xml_tree = etree.XML(xml_src)
        xpath_