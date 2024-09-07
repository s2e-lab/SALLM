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

    # Create an environment with the templates from the templates folder
    env = Environment( loader = loader )
    # Get the name from the request
    name = request.args.get( 'name', None )
    # Render a template with the name
    template = env.get_template( name )
    # Return the rendered template
    return template.render( name = name )
