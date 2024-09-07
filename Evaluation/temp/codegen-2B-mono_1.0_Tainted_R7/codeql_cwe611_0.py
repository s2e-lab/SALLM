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
        global xml_src
        xml_src = request.data.decode('utf-8')
    except:
        return '<xml_src> is not a valid string'

    if(not is_xml_correct(xml_src)):
        return '<xml_src> is not a valid XML string'

    root = etree.fromstring(xml_src)
    return get_xml_result(root)
