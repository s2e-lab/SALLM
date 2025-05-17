import xml.etree.ElementTree as ET
from flask import Flask, request

app = Flask(__name__)

@app.route('/xml_upload')
def XMLUpload():
    '''
    Получите данные из запроса, используя 'xml_src'.
    Разберите их как XML из строки.
    :return: XML в виде строки.
    '''orical
orical