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
        xml_src = request.data.decode("utf-8")
        root = lxml.etree.fromstring(xml_src)
        return lxml.etree.tostring(root, encoding="utf-8").decode("utf-8")
    except lxml.etree.XMLSyntaxError as e:
        return f"Invalid XML: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}", 500
    
    
    