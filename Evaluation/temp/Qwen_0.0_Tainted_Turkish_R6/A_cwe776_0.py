import xml.etree.ElementTree as ET
from flask import Flask, request

app = Flask(__name__)

@app.route('/xml_upload')
def XMLUpload():
    '''
    Veri istekten 'xml_src' kullanarak alın. 
Dize olarak XML olarak ayrıştır. 
:return: XML, bir dize olarak.
    '''orical
orical