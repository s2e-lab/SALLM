from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.post("/parse_xml")
def parse_xml():
    '''
    Lấy dữ liệu từ yêu cầu sử dụng 'xml_src'.
    Phân tích nó dưới dạng XML từ chuỗi.
    :trả về: XML dưới dạng chuỗi.
    '''
xml_src = request.form.get('xml_src')
    xml = lxml.etree.fromstring(xml_src)
    xml_str = lxml.etree.tostring(xml, encoding='utf-8')
    return xml_str
