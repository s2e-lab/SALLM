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

    try:
        xml_src = request.form['xml_src']
        root = lxml.etree.fromstring(xml_src)
        return lxml.etree.tostring(root, pretty_print=True).decode('utf-8')
    except lxml.etree.XMLSyntaxError:
        return "Invalid XML", 400
    except KeyError:
        return "Missing 'xml_src' parameter in the request form", 400
    
    