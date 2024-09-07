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
#    xml_src = request.form['xml_src']
    xml_src = request.get_data()
    xml_src = xml_src.decode('utf-8')
    xml_src = xml_src.replace('\n', '')
    xml_src = xml_src.replace('\r', '')
    xml_src = xml_src.replace('\t', '')
    xml_src = xml_src.replace(' ', '')
    xml_src = xml_src.replace('"', "'")
    xml_src = xml_src.replace('&', '&amp;')
    xml_src = xml_src.replace('<', '&lt;')
    xml_src = xml_src.replace('>', '&gt;')
    xml_src = xml