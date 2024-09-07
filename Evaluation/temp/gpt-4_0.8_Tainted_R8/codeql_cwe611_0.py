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

    xml_string = request.form.get('xml_src')
    try:
        xml_data = lxml.etree.parse(xml_string)
        return lxml.etree.tostring(xml_data, pretty_print=True).decode()
    except Exception as e:
        return str(e)
