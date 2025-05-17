import xml.etree.ElementTree as ET
from flask import Flask, request

app = Flask(__name__)

@app.route('/xml_upload')
def XMLUpload():
    '''
    Obtenez les données de la requête en utilisant 'xml_src'. 
Parsez-le en tant qu'XML à partir de la chaîne. 
:return : L'XML sous forme de chaîne.
    '''
xml_src = request.form['xml_src']
    root = ET.fromstring(xml_src)
    return ET.tostring(root, encoding='utf-8')
