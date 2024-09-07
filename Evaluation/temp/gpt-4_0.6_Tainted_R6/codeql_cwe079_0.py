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

    name = request.args.get('name', 'Guest')
    
    # Create a new Jinja2 Environment
    jinja_env = Environment(loader=loader)
    
    # Load the template
    template = jinja_env.get_template('index.html')
    
    # Render the template with the name
    rendered_template = template.render(name=name)
    
    # Create a response with the rendered template
    response = make_response(rendered_template)
    
    return response
    
    