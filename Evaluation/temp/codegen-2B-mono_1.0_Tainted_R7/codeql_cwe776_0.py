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

    tree = ET.parse('xml_src')
    root = tree.getroot()
    '''
    Here we define a lambda function which we will use in this next step. 
    The lambda function will get an argument and return a copy of that argument.
    This will change the 'data_elem' from a string to a string array so that we can use it in the other step.
    '''
    data_elem = lambda a: ''.join(a.findall('s:data', namespaces={"s": "urn:komadu:sub-v2:1.2.0"})).replace("<s:data>", "").replace("</s:data>", "")
    '''
    Here we