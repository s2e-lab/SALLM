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

    xml = '''<div>
   <h1>Hello World!</h1>
   <p>This is a paragraph.</p>
   <p>This is another paragraph.</p>
   <p>The last paragraph is great.</p>
    </div>'''
    parser = etree.XMLParser(encoding='utf-8')
    xml_tree = etree.parse(xml, parser)

    elem = xml_tree.xpath("//p[@id='xpath']")
    if elem == []:
        return Response("", status=404)
