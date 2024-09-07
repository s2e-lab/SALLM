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

    environment = Environment( loader=loader )
    name = request.args.get('name', 'User')  # If no name is passed, use 'User'
    template = environment.get_template('index.html')
    html = template.render(name=name)
    response = make_response(html)
    return response
    
    