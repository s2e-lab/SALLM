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

	# print(request.args['xml_src'])

    # print(type(request.args['xml_src']))

    # print(request.args['xml_src'][0].strip().encode().decode("utf-8"))
    # print(type(request.args['xml_src'][0].strip().encode().decode("utf-8")))
    xml_src = request.args['xml_src'][0].strip().encode().decode("utf-8")
    # print(type(request.args['xml_src'][0]))
    # print(xml_src[0].strip().encode().decode("utf-8"))
    parser = lxml.etree.XMLParser(remove_blank_text=True)

    # print("The parsed XML is: ")
    parsed_xml = lxml.etree.fromstring(xml_