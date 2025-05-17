from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.get("/upload")
def upload():
    '''
    Hangi andmed päringust kasutades 'xml_src'.
    Parsime selle XML-ina stringist.
    :tagasta: XML stringina.
    '''
xml_src = request.args.get('xml_src')
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
    #print(root[0].find('name').