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

    # Get name from the request.
    name = request.args.get('name', '')
    # Load the template.
    template = loader.get_template("index.html")
    # Render the template and render the name from the request.
    return template.render(name=name)
