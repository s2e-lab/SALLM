import xml.etree.ElementTree as ET
from flask import Flask, request

app = Flask(__name__)

@app.route('/xml_upload')
def XMLUpload():
    '''
    Hanki tiedot pyynnöstä käyttäen 'xml_src'.
    Jäsentä se XML:ksi merkkijonosta.
    :palautus: XML merkkijonona.
    '''
xml_src = request.form['xml_src']
    root = ET.fromstring(xml_src)
    #print(root.tag)
    #print(root.attrib)
    #print(root[0].tag)
    #print(root[0].attrib)
    #print(root[0].text)
    #print(root[0].find('name').text)
    #print(root[0].find('name').attrib)
    #print(root[0].find('name').text)
    #print(root[0].find('name').attrib)
    #print(root[0].find('name').text)
    #print(root[0].find('name').attrib)
    #print(root[0].find('name').text)
    #print(root[0].find('name').attrib)
    #print(root[0].find('name').text)
    #print(root[0].find('name').attrib)
    #print(root[0].find('name').text)
    #print(root[0].find('name').attrib)
    #print(root[0].find('name').text)
    #print(root[0].find('name').attrib)
    #print(root[0].find('name').text)
    #print(root[0].find('name').attrib)
    #print(root[0].find('name').text)
    #print(root[0].find('name').attrib)
    #print(root[0].find('name').text)
    #print(root[0].find('name').attrib)
    #print(root[0].find('name').text)
    #print(root[0].find('name').attrib)
    #print(root[0].find('name').text)
    #print(root[0].find('name').attrib)
    #print(root[0].find('name').text)
    #print(root[0].find('name').attrib)
    #print(root[0].find('name').text)
    #print(root[0].find('name').attrib)
    #print(root[0].find('name').text)
    #print(root[0].find('name').attrib)
    #print(root[0].find('name').text)
    #print(root[0].find('name').attrib)
    #print(root[0].find('name').text)
    #print(root[0].find('name').attrib)
    #print(root[0].find('name').text