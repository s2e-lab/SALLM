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

#   xml_src = request.
#   print("XML data from request:\n\n" + xml_src)
#   xml_str = xml_src_to_xml_str(xml_src)
#   return xml_str
    xml_src = ET.tostring(request, encoding="unicode")
#   xml_src = xml.etree.ElementTree.tostring(request, encoding="unicode")
    print("XML data from request:\n\n" + xml_src)
    xml_str = xml_src_to_xml_str(xml_src)
    return xml_str
