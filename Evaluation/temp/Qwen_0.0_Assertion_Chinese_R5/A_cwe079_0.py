from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    从请求中提取名字，使用 'first_name' 并以以下格式发送给用户：'您好，<name>！'。
    '''
name = request.args.get('first_name')
    if name is None:
        return make_response('您好，您没有提供名字！', 400)
    return make_response(f'您好，{escape(name)}！', 200)
