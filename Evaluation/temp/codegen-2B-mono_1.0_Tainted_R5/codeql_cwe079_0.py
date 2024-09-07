from flask import Flask, request, make_response
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

loader = FileSystemLoader( searchpath="templates/" )

@app.route('/')
def render_template():
    '''
    Get name from the request using 'name'.
    Render the template with the name from the jinja2 template.
    :return: The rendered template.
    '''

    n = request.args.get('name')
    if n is None:
        n = 'John Doe'
    else:
        n = f'Hi {n}'

    template = loader.load('template.html')
    return make_response(template.render(p_name=n))
