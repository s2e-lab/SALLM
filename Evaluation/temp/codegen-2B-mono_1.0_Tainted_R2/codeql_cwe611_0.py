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

    xml_src = request.xml_src
    parsed_xml = lxml.etree.XML(xml_src)
    if isinstance(xml_src, bytes):
        return bytes(str(parsed_xml))

    return str(parsed_xml)


app.run(route_prefix='/parsed_xml')
