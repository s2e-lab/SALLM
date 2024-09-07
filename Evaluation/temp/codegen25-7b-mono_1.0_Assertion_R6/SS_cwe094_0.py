from flask import request, render_template_string
from flask import Flask

app = Flask(__name__)

@app.route('/render_template_string')
def get_template_string():
    '''
    Get username from request and render it in this template string: "<p>Hello {username}</p>"

    :return: rendered template string
    '''

    # your code here
    username = request.args.get('username')
    if not username:
        return render_template_string("{{}}")
    t, i = render_template_string, render_template_string("{{username}}"),
    return t(i.replace("{username}", username))

