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

    xml_src = request.get_data()
    xml_src = xml_src.decode('utf-8')
    xml_src = lxml.etree.fromstring(xml_src)
    xml_src = lxml.etree.tostring(xml_src, pretty_print=True, encoding=str)
    return xml_src

