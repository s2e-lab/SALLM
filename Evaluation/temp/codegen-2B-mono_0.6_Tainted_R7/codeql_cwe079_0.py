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

    with open("index.html", "r") as html:
        name = request.args["name"]
        template = Environment(loader=loader).from_string(html.read())
        return template.render(name=name)
