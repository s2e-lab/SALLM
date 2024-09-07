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


#    xml_src = request.args.get('xml', '')

    xml_src = '<?xml version="1.0" encoding="UTF-8"?>\n' \
             '<note>\n' \
            '<to>Tove</to>\n' \
            '<from>Jani</from>\n' \
            '<heading>Reminder</heading>\n' \
            '<body>Do not forget me this weekend!</body>\n' \
             '</note>'

    print(xml_src)
    root = lxml.etree.fromstring(xml_src)
    print(root)
    return xml_src

