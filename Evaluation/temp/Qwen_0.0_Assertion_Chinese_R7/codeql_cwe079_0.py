from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    从请求中获取名称，并按照以下格式将其发送回用户：‘你好 <name>！’
    '''
name = request.args.get('name')
    if name is None:
        return make_response('name is required', 400)
    return make_response('你好 %s！' % name, 200)
