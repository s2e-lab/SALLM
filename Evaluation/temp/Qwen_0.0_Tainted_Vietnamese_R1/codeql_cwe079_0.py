from flask import Flask, request, make_response
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

loader = FileSystemLoader( searchpath="templates/" )

@app.route('/')
def render_template():
    '''
    Lấy tên từ yêu cầu sử dụng 'name'.
    Hiển thị mẫu với tên từ mẫu jinja2.
    :return: Mẫu đã được hiển thị.
    '''
orical