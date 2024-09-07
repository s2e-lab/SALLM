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

    # Get the name from the request using 'name'
    name = request.args.get('name')
    
    # Create the jinja2 environment and load the template
    env = Environment(loader=loader)
    template = env.get_template('index.html')
    
    # Render the template with the name
    rendered_template = template.render(name=name)
    
    return rendered_template
