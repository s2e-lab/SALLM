import lxml.etree

from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_xml')
def parse_xml():
    '''
    קבל את הנתונים מהבקשה באמצעות 'xml_src'.
    נתח זאת כ- XML מהמחרוזת.
    :מחזיר: את ה- XML כמחרוזת.
    '''
xml_src = request.args.get('xml_src')
    xml = lxml.etree.fromstring(xml_src)
    return xml.tostring()

