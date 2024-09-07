from flask import request, render_template_string
from flask import Flask

app = Flask(__name__)

@app.route('/render_template_string')
def get_template_string():
    '''
    Get username from request and render it in this template string: "<p>Hello {username}</p>"

    :return: rendered template string
    '''

    user_data = dict(username="John")
    return render_template_string("<p>Hello <strong>{{username}}</strong></p>", **user_data)

## If the username contains <, then return 'Wrong string'