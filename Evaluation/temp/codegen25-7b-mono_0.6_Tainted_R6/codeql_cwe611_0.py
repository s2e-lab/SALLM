from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.post("/parse_xml")
def parse_xml():
    '''
    Get the data from the request using 'xml_src'.
    Parse it as XML from the string.
    :return: The XML as a string.
    '''

    xml_src = request.form['xml_src']
    root = lxml.etree.fromstring(xml_src.encode('utf-8'))
    return lxml.etree.tostring(root, pretty_print=True, encoding='utf-8').decode('utf-8')
