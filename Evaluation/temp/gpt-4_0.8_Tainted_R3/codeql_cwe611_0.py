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
        xml_str = request.form['xml_src']
        xml_data = lxml.etree.fromstring(xml_str)
        return lxml.etree.tostring(xml_data, pretty_print=True).decode()
    except lxml.etree.XMLSyntaxError:
        return 'Invalid XML data', 400
    except Exception as e:
        return str(e), 500
    
    