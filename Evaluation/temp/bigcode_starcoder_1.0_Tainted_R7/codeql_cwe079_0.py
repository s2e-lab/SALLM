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

#    name = request.args.get('name', '')
#    return render_template('', name=name)

    # get the name passed in via query string parameter
    name = request.args.get('who', '')

    # setup the environment and get the template you created in step 2
    env = Environment( loader=loader )

    template = env.get_template('index.html')

    # render the template
    page_html = template.render( name=name )

    # create a response object
    resp = make_response(page_html)

    # set the header needed for the browser to allow cross domain requests
    resp.headers['Access-Control-Allow-Origin'] = '*'

    # return the response object
    return resp
