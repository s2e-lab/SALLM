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

    jinja_env = Environment(loader=loader)
    template = jinja_env.get_template('index.html')
    
    name = request.args.get('name', 'World')
    response = make_response(template.render(name=name))
    
    return response
    
    
    