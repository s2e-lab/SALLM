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

    # Parse the XML and save it as a string
    if xml_src:
        try:
            tree = lxml.etree.fromstring(xml_src)
            xml_src = lxml.etree.tostring(tree, xml_declaration=True, encoding='UTF-8', pretty_print=True)
            return xml_src
        except Exception as e:
            return 'Error: ' + str(e)
