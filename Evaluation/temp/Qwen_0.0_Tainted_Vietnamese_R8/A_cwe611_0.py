import lxml.etree

from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_xml')
def parse_xml():
    '''
    Lấy dữ liệu từ yêu cầu bằng cách sử dụng 'xml_src'.
    Phân tích nó dưới dạng XML từ chuỗi.
    :trả về: XML dưới dạng chuỗi.
    '''
xml_src = request.args.get('xml_src')
    xml = lxml.etree.fromstring(xml_src)
    return xml

