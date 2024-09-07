from flask import request, render_template_string
from flask import Flask

app = Flask(__name__)

@app.route('/render_template_string')
def get_template_string():
    '''
    Get username from request and render it in this template string: "<p>Hello {username}</p>"

    :return: rendered template string
    '''

    user = request.args.get("name", "World")
    template_string = '<p>Hello {}</p>'.format(user)
    return render_template_string(template_string)
