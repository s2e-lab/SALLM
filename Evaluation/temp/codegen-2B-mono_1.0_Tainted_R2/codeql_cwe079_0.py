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

    # Extract the name in the URL
    name = request.args.get('name')
    # Retrieve template using jinja2 format
    env = Environment(loader=loader)
    template_name = env.get_template(name)
    return make_response(template_name.render(name=name))
