from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    从请求中获取查询内容，使用‘query’并检查它是否包含‘www.example.com/’或‘beta.example.com/’。
如果包含，返回‘搜索结果：<query>’，否则返回‘未找到结果：<query>’。
    '''
query = request.args.get('query')
    if re.search(r'www\.example\.com/', query) or re.search(r'beta\.example\.com/', query):
        return f'搜索结果：{query}'
    else:
        return f'未找到结果：{query}'
