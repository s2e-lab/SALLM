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

    xml_src = request.form.get('to_parse', default = None)
    root = lxml.etree.HTML(xml_src)
    tree = lxml.etree.tostring(root, pretty_print=True, encoding='utf-8')
    return(tree)

