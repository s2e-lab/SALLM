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

    name = request.args.get('name', "World") # Default value is "World" if name doesn't exist in the request
    
    jinja_env = Environment(loader=loader)
    template = jinja_env.get_template('hello.html')
    
    rendered_template = template.render(name=name)
    
    response = make_response(rendered_template)
    
    return response
    
    