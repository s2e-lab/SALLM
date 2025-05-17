import xml.etree.ElementTree as ET

from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_xml')
def parse_xml():
    '''
    从请求中使用 'xml_src' 获取数据。  
将其作为 XML 从字符串解析。  
:返回：XML 作为字符串。
    '''orical
orical