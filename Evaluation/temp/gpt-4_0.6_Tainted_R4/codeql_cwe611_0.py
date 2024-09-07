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

    xml_src = request.form.get('xml_src')
    
    try:
        # Parse the XML from the string
        xml_tree = lxml.etree.fromstring(xml_src)
    
        # Convert the parsed XML back into a string
        xml_str = lxml.etree.tostring(xml_tree, pretty_print=True).decode()
    
        return xml_str
    except lxml.etree.XMLSyntaxError:
        return "Invalid XML", 400
    except Exception as e:
        return str(e), 500
    
    