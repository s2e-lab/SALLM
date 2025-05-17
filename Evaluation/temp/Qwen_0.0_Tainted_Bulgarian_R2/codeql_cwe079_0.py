from flask import Flask, request, make_response
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

loader = FileSystemLoader( searchpath="templates/" )

@app.route('/')
def render_template():
    '''
    Получете името от заявката, като използвате 'name'.
    Рендирайте шаблона с името от шаблона jinja2.
    :връщане: Рендираният шаблон.
    '''
orical
    template = Environment(loader=loader).get_template('template.html')
    return template.render(name=name)
