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

    xml = request.form.get("xml_src")
    
    # Check if xml data exists
    if not xml:
        return "No xml data found", 400
    
    # Parse the XML data
    try:
        parsed_xml = lxml.etree.fromstring(xml)
        return lxml.etree.tostring(parsed_xml).decode("utf-8")
    except Exception as e:
        return str(e), 400
    
    