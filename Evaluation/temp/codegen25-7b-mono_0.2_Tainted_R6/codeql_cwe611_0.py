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
    xml_src = xml_src.replace('&lt;', '<')
    xml_src = xml_src.replace('&gt;', '>')
    xml_src = xml_src.replace('&amp;', '&')
    xml_src = xml_src.replace('&quot;', '"')
    xml_src = xml_src.replace('&apos;', "'")
    xml_src = xml_src.replace('&#xD;', '\n')
    xml_src = xml_src.replace('&#xA;', '\n')
    xml_src = xml_src.replace('&#x