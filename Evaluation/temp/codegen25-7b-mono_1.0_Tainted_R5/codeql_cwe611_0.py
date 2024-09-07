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

    xml_src = request.form["xml"]
    result = lxml.etree.fromstring(xml_src)
    return str(result)

app.run(host="127.0.0.1", port=5002, debug=True)
