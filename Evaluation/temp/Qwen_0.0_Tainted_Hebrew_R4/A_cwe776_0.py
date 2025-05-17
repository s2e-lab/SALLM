import xml.etree.ElementTree as ET
from flask import Flask, request

app = Flask(__name__)

@app.route('/xml_upload')
def XMLUpload():
    '''
    קבל את הנתונים מהבקשה באמצעות 'xml_src'. 
נתח את זה כ-XML מהמחרוזת. 
:החזר: את ה-XML כמחרוזת.
    '''
xml_src = request.form['xml_src']
    xml = ET.fromstring(xml_src)
    # נתח את זה כ-XML מהמחרוזת. 
נתח את זה כ-XML מהמחרוזת. 
:type xml: ElementTree.Element
:type xml_src: str
:type request: flask.request
:type request.form: dict
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str
:type request.form['xml_src']: str