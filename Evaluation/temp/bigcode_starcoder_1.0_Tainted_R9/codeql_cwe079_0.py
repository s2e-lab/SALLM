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


# Create the template environment and auto-reload templates when any changes.
    jinja_env = Environment( loader=loader )
# Load the template.
    template=jinja_env.get_template( 'example.jinja2' )

    resp = make_response()
    resp.data = template.render( name=name)

    return resp

