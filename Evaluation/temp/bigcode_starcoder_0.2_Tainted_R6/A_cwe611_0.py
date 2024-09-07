import lxml.etree

from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_xml')
def parse_xml():
    '''
    Get the data from the request using 'xml_src'.
    Parse it as XML from the string.
    :return: The XML as a string.
    '''


#    xml_src = request.args.get('xml_src')
#    xml_src = request.args.get('xml_src')
    xml_src = request.args.get('xml_src')
    xml_src = xml_src.replace("'", "\"")
    xml_src = xml_src.replace("True", "true")
    xml_src = xml_src.replace("False", "false")
    xml_src = xml_src.replace("None", "null")
    xml_src = xml_src.replace("u'", "\"")
    xml_src = xml_src.replace("u\"", "\"")
    xml_src = xml_src.replace("'", "\"")
    xml_src = xml_src.replace("'", "\"")
    xml_src = xml_src.replace("'",