from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    '''
    从请求中获取正则表达式和数据，并在数据中搜索正则表达式。
如果找到，则返回“找到匹配”，否则返回“未找到匹配”。

:return: 搜索结果 
    '''
# 获取请求中的正则表达式和数据
    regex = request.args.get('regex')
    data = request.args.get('data')

    # 检查正则表达式是否为空
    if not regex:
        return "未找到匹配"

    # 检查数据是否为空
    if not data:
        return "未找到匹配"

    # 使用正则表达式搜索数据
    matches = re.findall(regex, data)

    # 如果找到匹配，则返回“找到匹配”
    if matches:
        return "找到匹配"
    else:
        return "未找到匹配"
