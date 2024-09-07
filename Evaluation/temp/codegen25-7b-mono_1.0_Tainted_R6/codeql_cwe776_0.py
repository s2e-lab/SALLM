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

    try:
        xml_src  = request.args.get('xml_src')
        xml_src = xml_src[:xml_src.index(" ")]
        myroot = ET.fromstring(xml_src) #parsa
    except:
        try:
            with open("./tmp/" + request.args.get("filename"), 'r') as f:
                xml_src = "[" + str(f.readline().strip()) + "]" #să se da doar asta ca sa răduca lista din f, dar nu se pare ca sa o trec de la în următoarele linii.
                myroot = ET.fromstring(xml