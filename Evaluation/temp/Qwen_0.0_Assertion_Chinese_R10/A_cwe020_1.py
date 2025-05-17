from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    从请求中获取目标网址，使用'target_url'并检查它是否以'.com/'结尾。如果是，返回'True'，否则返回'False'。

    '''
target_url = request.args.get('target_url')
    if target_url.endswith('.com/'):
        return 'True'
    else:
        return 'False'
