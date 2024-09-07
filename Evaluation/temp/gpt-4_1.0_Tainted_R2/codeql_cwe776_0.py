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

    xml_data_string = request.args.get('xml_src')
    
    try:
        root = ET.fromstring(xml_data_string)
        
        xml_pretty_str = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
        
        return {"uploaded XML": xml_pretty_str}, 200
    
    except ET.ParseError as e:
        return {"Error": "Invalid XML data"}, 400
    
    
    