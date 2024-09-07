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

#    env = Environment()
#    name = request.args.get('name')
#    template = env.from_string(app.send_static_file('./templates/welcome.html'))
#    html = template.render( name=name )
#    return html, 200
    return render_template('welcome.html'), 200

# This runs the flask app on port 80