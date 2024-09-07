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

    xml_src = '''<?xml version="1.0" encoding="UTF-8"?>
<data>
  <item>
    <id>1</id>
    <name>item1</name>
    <type>book</type>
    <price>1.00</price>
    <tags>
      <tag>
        <id>1</id>
        <name>tag1</name>
      </tag>
      <tag>
        <id>2</id>
        <name>tag2</name>
      </tag>
    </tags>
