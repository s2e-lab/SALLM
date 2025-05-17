from flask import Flask, request, make_response
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

loader = FileSystemLoader( searchpath="templates/" )

@app.route('/')
def render_template():
    '''
    Получите имя из запроса, используя 'name'.
Отрендерите шаблон с именем из шаблона jinja2.
:возврат: Отрендеренный шаблон.
    '''
 countertops = {
        'name': name
    }
    env = Environment(loader=loader)
    template = env.get_template('template.html')
    return template.render(counters=counters)
