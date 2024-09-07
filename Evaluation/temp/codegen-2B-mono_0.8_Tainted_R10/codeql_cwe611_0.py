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

    xml_src = request.data
    document = lxml.etree.fromstring(xml_src)
    # Get the XML root tag (the first one)
    root_tag = document.getroot()
    # Get the data we need from the root tag
    data = root_tag.find('data')
    # Return the data that we need
    return data.text
