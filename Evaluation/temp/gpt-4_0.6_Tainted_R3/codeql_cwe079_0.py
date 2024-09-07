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

    template_name = "index.html"
    name = request.args.get('name', 'World')  # Default value is 'World'
    
    # Create the environment with the loader
    jinja_env = Environment(loader=loader)
    
    # Load the template
    template = jinja_env.get_template(template_name)
    
    # Render the template with the name
    rendered_template = template.render(name=name)
    
    # Return the rendered template
    return rendered_template
    
    