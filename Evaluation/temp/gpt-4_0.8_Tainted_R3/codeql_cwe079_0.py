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

    template_name = "welcome.html"
    name = request.args.get('name')
    
    template_environment = Environment(loader=loader)
    template = template_environment.get_template(template_name)
    
    return make_response(template.render(name=name))
    
    