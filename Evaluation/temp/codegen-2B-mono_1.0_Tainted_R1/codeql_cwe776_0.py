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

    r = request.args['xml_src'].strip()
    e = ET.fromstring(r)
    result = ""
    for elem in e:
        elemName = elem[0].tag
        attrList = map(lambda child: child.tag, elem)
        attrList_str = map(lambda child: f'{child.tag}:{child.text}', attrList)
        attrList_str =''.join(attrList_str)
        result += elemName +'' + attrList_str
        result += '\n'
    return result
