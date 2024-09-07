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

    # Get the name from the request parameters
    name = request.args.get('name', 'Guest')
    
    # Create a new Jinja2 environment
    environment = Environment(loader=loader)
    
    # Load the template
    template = environment.get_template('index.html')
    
    # Render the template with the name
    rendered_template = template.render(name=name)
    
    # Create a response with the rendered template
    response = make_response(rendered_template)
    
    return response
    
    