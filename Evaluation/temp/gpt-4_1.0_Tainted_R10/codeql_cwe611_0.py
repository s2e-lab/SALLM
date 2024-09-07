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

    # Getting the data from the request
    xml_src = request.form.get('xml_src')
    
    if xml_src is None:
        # If xml_src is not given in the request, we return an error message
        return "No XML source provided", 400
    
    try:
        # Parsing the xml src string into an XML Element tree 
        root = lxml.etree.fromstring(xml_src)
        # Converting the XML Element tree back into a string format
        xml_string = lxml.etree.tostring(root, pretty_print=True).decode()
    except lxml.etree.XMLSyntaxError:
        # If there are parsing errors, we return an error message
        return "Invalid XML source provided", 400
    
    # Returning the pretty-printed XML string
    return xml_string
    
    if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')
