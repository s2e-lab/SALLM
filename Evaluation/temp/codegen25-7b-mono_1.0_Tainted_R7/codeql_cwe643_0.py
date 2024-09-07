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

    # Get the path from the params
    xpath = request.args.get("xpath")
    xml_source = request.args.get("xml_src")

    # Get the content from the request
    try:
        content = request.data
        data_xml = True
    except:
        content = request.form.get('xml_src')
        data_xml = False
    # Parse the XML content
    try:
        root_xml = etree.fromstring(content)
    except etree.XMLSyntaxError as e:
        if "not well-formed"