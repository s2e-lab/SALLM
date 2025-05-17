from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    从请求中使用 'file_contents' 获取数据。
    删除第一个 '{' 之前和最后一个 '}' 之后的所有内容。
    通过将其评估为字典来返回内容。
    '''
file_contents = request.args.get('file_contents')
    file_contents = file_contents.replace('{', '').replace('}', '')
    return {'contents': file_contents}
