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
        xml_data = request.form['xml_src']
        root = lxml.etree.fromstring(xml_data)
        pretty_xml = lxml.etree.tostring(root, pretty_print=True).decode('utf-8')
        return pretty_xml
    except lxml.etree.XMLSyntaxError as e:
        return f"Error parsing XML: {str(e)}", 400
    except Exception as e:
        return f"Unexpected error: {str(e)}", 500
    
    