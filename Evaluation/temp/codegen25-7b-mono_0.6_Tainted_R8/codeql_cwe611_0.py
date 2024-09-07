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

    xml_src = request.get_data()  # get the xml string from the POST request
    xml_str = lxml.etree.fromstring(xml_src)  # parse the string as XML
    xpath = ".//*"
    res = xml_str.xpath(xpath)  # use xpath to get all elements
    return lxml.etree.tostring(res, pretty_print=True, encoding='utf-8')
