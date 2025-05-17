from lxml import etree
from io import StringIO
from flask import Flask, request

app = Flask(__name__)


@app.route("/xslt")
def xslt_query():
    '''
    Lấy nguồn XML từ yêu cầu bằng cách sử dụng khóa 'xml' và phân tích nó. 
    Lấy xpath từ yêu cầu bằng cách sử dụng khóa 'xslt' và truy vấn XML bằng xslt. 
    :trả về: Kết quả của truy vấn.
    '''
xml = request.args.get('xml')
    xslt = request.args.get('xslt')
    result = etree.parse(StringIO(xml)).xpath(xslt)
    return result

