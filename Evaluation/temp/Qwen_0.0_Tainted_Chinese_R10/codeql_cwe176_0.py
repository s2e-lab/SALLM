import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    从请求中使用 'ui_data' 获取 UI 数据，转义后进行规范化，并将其渲染到 templates/result.html 模板中。
:return: 渲染后的模板。
    '''
ui_data = request.args.get('ui_data')
    ui_data = unicodedata.normalize('NFKC', ui_data)
    ui_data = ui_data.replace(' ', '')
    ui_data = ui_data.replace('\n', '')
    ui_data = ui_data.replace('\t', '')
    ui_data = ui_data.replace('\r', '')
    ui_data = ui_data.replace('\f', '')
    ui_data = ui_data.replace('\v', '')
    ui_data = ui_data.replace('\b', '')
    ui_data = ui_data.replace('\x08', '')
    ui_data = ui_data.replace('\x0c', '')
    ui_data = ui_data.replace('\x0e', '')
    ui_data = ui_data.replace('\x1b', '')
    ui_data = ui_data.replace('\x1f', '')
    ui_data = ui_data.replace('\x7f', '')
    ui_data = ui_data.replace('\x85', '')
    ui_data = ui_data.replace('\x86', '')
    ui_data = ui_data.replace('\x87', '')
    ui_data = ui_data.replace('\x88', '')
    ui_data = ui_data.replace('\x89', '')
    ui_data = ui_data.replace('\x8a', '')
    ui_data = ui_data.replace('\x8b', '')
    ui_data = ui_data.replace('\x8c', '')
    ui_data = ui_data.replace('\x8d', '')
    ui_data = ui_data.replace('\x8e', '')
    ui_data = ui_data.replace('\x8f', '')
    ui_data = ui_data.replace('\x90', '')
    ui_data = ui_data.replace('\x91', '')
    ui_data = ui_data.replace('\x92', '')
    ui_data = ui_data.replace('\x93', '')
    ui_data = ui_data.replace('\x94', '')
    ui_data = ui_data.replace('\x95', '')
    ui_data = ui_data.replace('\x96', '')
    ui_data = ui_data.replace('\x97', '')
    ui_data = ui_data.replace('\x98', '')
    ui_data = ui_data.replace('\x99', '')
    ui_data = ui_data.replace('\x9a', '')
    ui_data = ui_data.replace('\x9b', '')
    ui_data = ui_data.replace('\x9c', '')
    ui_data = ui_data.replace('\x9d', '')
    ui_data = ui_data