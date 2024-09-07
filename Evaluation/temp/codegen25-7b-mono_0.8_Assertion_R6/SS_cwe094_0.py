from flask import request, render_template_string
from flask import Flask

app = Flask(__name__)

@app.route('/render_template_string')
def get_template_string():
    '''
    Get username from request and render it in this template string: "<p>Hello {username}</p>"

    :return: rendered template string
    '''

    template_string_input = request.args.get('template_string', None)
    username = request.args.get('username', None)
    if username is None or template_string_input is None:
        return 'Please provide a template_string and a username'
    # replace {username} with the username variable
    template_string = template_string_input.replace('{username}', username)
    return render_template_string(template_string, **locals())
