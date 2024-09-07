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

    name = request.args.get("name", "world")

    template = Environment( loader=loader ).get_template( 'template.txt' )
    rendered_template = template.render(name=name)

    resp = make_response(rendered_template, 200)
    resp.headers["Content-Type"] = 'application/text; charset=utf-8'
    return resp
