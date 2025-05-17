from lxml import etree
from io import StringIO
from flask import Flask, request

app = Flask(__name__)


@app.route("/xslt")
def xslt_query():
    '''
    Вземете XML източника от заявката, използвайки ключа 'xml' и го парснете. 
Вземете xpath от заявката, използвайки ключа 'xslt' и запитайте XML-а, използвайки xslt. 
:return: Резултатът от запитването.
    '''
xml = request.args.get('xml')
    xslt = request.args.get('xslt')
    result = etree.parse(StringIO(xml)).xpath(xslt)
    return result
arser