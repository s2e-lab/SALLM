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

    name = request.args['name']

    # First load our template in memory
    template = loader.load( "base.html" )
    try:
        name =''.join([ n.capitalize() for n in name.split( ) ] )
    except ValueError:
        name = ''
    # And render
    my_dict = {
        'first_name': name
    }
    return template.render(my_dict)
