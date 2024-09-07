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

    # TODO: Parse the xml_src as an xml from a string.
    
    # TODO: Return the xml as a string.
    return xml_src
