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

    xml_src = request.args.get('xml_src')
    root = ET.fromstring(xml_src)
    #print(root)
    data = {}
    for sub_root in root.iter('ROOT'):
        if sub_root.tag == 'ROOT':
            for entry in sub_root:
                if entry.tag == 'ROW':
                    data['ROW'] = {}
                    for child in entry:
                        if child.tag == 'IN':
                            data['ROW']["IN"] = {}
                            for child2 in child:
                                if child2.tag == 'ROW':
                                    data['ROW']["IN"]["ROW"] = {}
                                