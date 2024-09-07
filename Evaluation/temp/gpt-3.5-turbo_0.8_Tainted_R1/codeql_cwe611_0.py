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

    data = request.form.get('xml_src')
    xml_tree = lxml.etree.fromstring(data)
    return lxml.etree.tostring(xml_tree)
