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

    xml_src = request.args.get('xml_src')

    # Parse the request as XML
    xml_parsed = lxml.etree.fromstring(xml_src)

    # Get the root element
    root = xml_parsed.getroot()

    # Get the values to be returned
    return_val = {}
    for child in root:
        # Get the name of the child
        child_name = child.tag

        # Get the value
        child_value = child.text

        return_val[child_name] = child_value

    return str(return_val)

