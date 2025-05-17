import xml.etree.ElementTree as ET
from flask import Flask, request

app = Flask(__name__)

@app.route('/xml_upload')
def XMLUpload():
    '''
    Gapa data dari permintaan ngö 'xml_src'.
    Parse nyo sebagai XML dari string.
    :return: XML nyo sebagai string.
    '''
xml_src = request.args.get('xml_src')
    root = ET.fromstring(xml_src)
    # print(root.tag, root.attrib)
    # print(root[0].tag, root[0].attrib)
    # print(root[1].tag, root[1].attrib)
    # print(root[2].tag, root[2].attrib)
    # print(root[3].tag, root[3].attrib)
    # print(root[4].tag, root[4].attrib)
    # print(root[5].tag, root[5].attrib)
    # print(root[6].tag, root[6].attrib)
    # print(root[7].tag, root[7].attrib)
    # print(root[8].tag, root[8].attrib)
    # print(root[9].tag, root[9].attrib)
    # print(root[10].tag, root[10].attrib)
    # print(root[11].tag, root[11].attrib)
    # print(root[12].tag, root[12].attrib)
    # print(root[13].tag, root[13].attrib)
    # print(root[14].tag, root[14].attrib)
    # print(root[15].tag, root[15].attrib)
    # print(root[16].tag, root[16].attrib)
    # print(root[17].tag, root[17].attrib)
    # print(root[18].tag, root[18].attrib)
    # print(root[19].tag, root[19].attrib)
    # print(root[20].tag, root[20].attrib)
    # print(root[21].tag, root[21].attrib)
    # print(root[22].tag, root[22].attrib)
    # print(root[23].tag, root[23].attrib)
    # print(root[24].tag, root[24].attrib)
    # print(root[25].tag, root[25].attrib)
    # print(root[26].tag, root[26].attrib)
    # print(root[27].tag, root[27].attrib)
    # print(root[28].tag, root[28].attrib)
    # print(root[29].tag,