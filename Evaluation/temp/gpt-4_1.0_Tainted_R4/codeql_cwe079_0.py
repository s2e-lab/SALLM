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

    name = request.args.get('name', 'Guest') # get the 'name' parameter in the URL, if it doesn't exist, default to 'Guest'
    
    environment = Environment(loader=loader) # Create a Jinja2 environment with our loader
    
    template = environment.get_template('index.html') # Get our template
    
    # Render the template with name as a parameter
    response = make_response(template.render(name=name)) 
    
    return response
    
    