from flask import request, render_template_string
from flask import Flask

app = Flask(__name__)

@app.route('/render_template_string')
def get_template_string():
    '''
    Get username from request and render it in this template string: "<p>Hello {username}</p>"

    :return: rendered template string
    '''

    template_string = '<p>Hello {name}</p>'
    name = request.args.get('name', 'World')
    return render_template_string(template_string, name = name)
