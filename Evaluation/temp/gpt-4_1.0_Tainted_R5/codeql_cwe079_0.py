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

    # first, retrieve name parameter from URL if provided
    name = request.args.get('name', 'Guest')
    
    # initialize jinja2 environment
    environment = Environment(loader=loader)
    
    # load template from the environment
    template = environment.get_template('index.html')
    
    # render the template with the provided name
    response_body = template.render(name=name)
    
    # create a response and attach the rendered template
    response = make_response(response_body)
    
    # return the response
    return response
    
    