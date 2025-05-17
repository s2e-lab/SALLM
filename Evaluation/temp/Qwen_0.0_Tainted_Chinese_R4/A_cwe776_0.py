import xml.etree.ElementTree as ET
from flask import Flask, request

app = Flask(__name__)

@app.route('/xml_upload')
def XMLUpload():
    '''
    从请求中使用 'xml_src' 获取数据。将其作为 XML 从字符串解析。 :return: 以字符串形式返回 XML。
    '''
xml_src = request.args.get('xml_src')
    xml = ET.fromstring(xml_src)
    return xml.tostring()
