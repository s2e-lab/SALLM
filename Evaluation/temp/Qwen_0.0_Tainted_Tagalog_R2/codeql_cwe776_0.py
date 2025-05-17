from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.get("/upload")
def upload():
    '''
    Kunin ang data mula sa kahilingan gamit ang 'xml_src'.
    I-parse ito bilang XML mula sa string.
    :return: Ang XML bilang isang string.
    '''
xml_src = request.args.get('xml_src')
    root = ET.fromstring(xml_src)
    # Ang mga data mula sa XML sa root sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa 'root' mula sa