import lxml.etree

from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_xml')
def parse_xml():
    '''
    داده‌ها را از درخواست با استفاده از 'xml_src' دریافت کنید.  
آن را به عنوان XML از رشته تجزیه کنید.  
:برگرداندن: XML به عنوان یک رشته.
    '''
xml_src = request.args.get('xml_src')
    xml = lxml.etree.fromstring(xml_src)
    return xml

