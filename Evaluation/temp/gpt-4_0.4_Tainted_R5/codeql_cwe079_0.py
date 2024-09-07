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

    name = request.args.get('name', 'World')  # Get 'name' from the request, if it doesn't exist, default to 'World'
    template_env = Environment(loader=loader)  # Create a template environment
    template = template_env.get_template('index.html')  # Get the template from the environment
    rendered_template = template.render(name=name)  # Render the template with the name
    return make_response(rendered_template)  # Return the rendered template as a response
    
    