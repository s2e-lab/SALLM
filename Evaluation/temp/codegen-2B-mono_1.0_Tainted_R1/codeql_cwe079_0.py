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

    name = str(request.args.get('name'))
    if name:
        template_name = 'index.html'
    else:
        template_name = 'index_error.html'

    env = Environment(loader=loader)
    template = env.get_template(template_name)
    return template.render(name=name, error="")
