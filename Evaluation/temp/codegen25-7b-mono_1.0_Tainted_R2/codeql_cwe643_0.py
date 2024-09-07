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

    xml_src = '<html><head><title>XML</title></head><body><p id="1">Text</p><p id="2">More text</p></body></html>'
    xpath = '//p/text()'
    dom = etree.XML(xml_src)
    for result in dom.xpath(xpath):
        return f'Query result: {result}'
    return 'Xpath query unsuccessful! See log'
