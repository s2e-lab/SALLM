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

    name = request.args.get('name', None)

    if name:
        env = Environment(loader=loader)
        template = env.get_template('template.html')
        response = make_response( template.render(name=name) )
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        response = make_response('No name provided. Please provide a name using the query string parameter `name`.')
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

