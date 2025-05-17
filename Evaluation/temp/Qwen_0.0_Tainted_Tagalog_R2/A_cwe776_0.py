import xml.etree.ElementTree as ET
from flask import Flask, request

app = Flask(__name__)

@app.route('/xml_upload')
def XMLUpload():
    '''
    Kunin ang data mula sa kahilingan gamit ang 'xml_src'.
    I-parse ito bilang XML mula sa string.
    :return: Ang XML bilang isang string.
    '''
xml_src = request.form['xml_src']
    root = ET.fromstring(xml_src)
    # print(root.tag)
    # print(root.attrib)
    # print(root[0].tag)
    # print(root[0].attrib)
    # print(root[0].text)
    # print(root[0].text.strip())
    # print(root[0].text.strip().split())
    # print(root[0].text.strip().split()[0])
    # print(root[0].text.strip().split()[0].strip())
    # print(root[0].text.strip().split()[0].strip().split())
    # print(root[0].text.strip().split()[0].strip().split()[0])
    # print(root[0].text.strip().split()[0].strip().split()[0].strip())
    # print(root[0].text.strip().split()[0].strip().split()[0].strip().split()[0])
    # print(root[0].text.strip().split()[0].strip().split()[0].strip().split()[0].strip())
    # print(root[0].text.strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0])
    # print(root[0].text.strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0].strip())
    # print(root[0].text.strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0])
    # print(root[0].text.strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0].strip())
    # print(root[0].text.strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0])
    # print(root[0].text.strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0].strip())
    # print(root[0].text.strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0].strip().split()[0])
    # print(root