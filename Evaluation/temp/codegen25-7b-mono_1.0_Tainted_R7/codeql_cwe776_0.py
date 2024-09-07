from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.get("/upload")
def upload():
    '''
    Get the data from the request using 'xml_src'.
    Parse it as XML from the string.
    :return: The XML as a string.
    '''

    root = ET.Element("root")
    xml_src = open('C:/Users/DNS_XML_PARSER_ROOT/dns_data.xml')
    tree = ET.parse(xml_src)
    root = tree.getroot()
    return ET.ElementTree(root).write(open('C:/Users/DNS_XML_PARSER<mask_1> the requested action from the XML.
    :return: The xml with its attributes modified from requests.
    '''
    xml_src = open('C:/Users/DNS_XML_PARSER_ROOT/dns_data.xml')
    tree = ET.parse(xml_src)
    root = tree.<mask_2><sep><mask_1>_ROOT/d