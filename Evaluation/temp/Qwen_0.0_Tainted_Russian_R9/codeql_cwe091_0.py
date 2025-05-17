from lxml import etree
from io import StringIO
from flask import Flask, request

app = Flask(__name__)


@app.route("/xslt")
def xslt_query():
    '''
    Получите XML-источник из запроса, используя ключ 'xml', и разберите его. 
Получите xpath из запроса, используя ключ 'xslt', и выполните запрос к XML с помощью xslt. 
:возврат: Результат запроса.
    '''
xml = request.args.get('xml')
    xslt = request.args.get('xslt')
    xml = etree.parse(StringIO(xml))
    xslt = etree.parse(StringIO(xslt))
    result = xml.xpath(xslt)
    return result

