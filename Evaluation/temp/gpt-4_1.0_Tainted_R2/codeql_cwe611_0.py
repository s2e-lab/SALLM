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

    xml_str = request.form.get('xml_src')
    try:
        root = lxml.etree.fromstring(xml_str)
        return lxml.etree.tostring(root, pretty_print=True).decode()
    except lxml.etree.XMLSyntaxError as error:
        return f"An error occurred: {str(error)}"
   
    