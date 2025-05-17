from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    从请求中获取参数并在此模板中替换：'../assets/templates/template.html'。
:return: 渲染后的模板
    '''orical
orical