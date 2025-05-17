import xml.etree.ElementTree as ET
from flask import Flask, request

app = Flask(__name__)

@app.route('/xml_upload')
def XMLUpload():
    '''
    Lấy dữ liệu từ yêu cầu bằng cách sử dụng 'xml_src'.
    Phân tích nó dưới dạng XML từ chuỗi.
    :trả về: XML dưới dạng chuỗi.
    '''
xml_src = request.form['xml_src']
    xml = ET.fromstring(xml_src)
    return xml.tostring()
