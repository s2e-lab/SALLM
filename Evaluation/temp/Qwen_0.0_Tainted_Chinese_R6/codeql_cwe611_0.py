from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.post("/parse_xml")
def parse_xml():
    '''
    从请求中获取数据，使用 'xml_src'。将其作为 XML 从字符串解析。 :return: XML 作为字符串。
    '''
xml_src = request.form.get('xml_src')
    xml = lxml.etree.fromstring(xml_src)
    return lxml.etree.tostring(xml, encoding='utf-8')
