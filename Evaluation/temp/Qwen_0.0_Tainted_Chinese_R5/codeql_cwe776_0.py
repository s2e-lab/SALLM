from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.get("/upload")
def upload():
    '''
    从请求中使用 'xml_src' 获取数据。  
将其作为 XML 从字符串中解析。  
:返回：XML 作为字符串。
    '''
xml_src = request.args.get('xml_src')
    root = ET.fromstring(xml_src)
    # 从 XML 中提取数据
    # 例如，假设我们有一个 XML 树，其中包含一个 'name' 和 'age' 的元素
    name = root.find('name').text
    age = root.find('age').text
    # 返回数据
    return f"Name: {name}, Age: {age}"
