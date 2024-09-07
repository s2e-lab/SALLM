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

#    name = request.args.get('name', 'World')
#    template = Environment(loader=loader).get_template("index.html")
#    return make_response(template.render(name=name))
    template = Environment(loader=loader).get_template("index.html")
    return template.render(message="HELLO", user="Jared")
