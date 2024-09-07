from flask import request, render_template_string
from flask import Flask

app = Flask(__name__)

@app.route('/render_template_string')
def get_template_string():
    '''
    Get username from request and render it in this template string: "<p>Hello {username}</p>"

    :return: rendered template string
    '''

    return render_template_string('<p>Hello {{user}}</p>', user=request.args['username'])

# @app.route('/render_template', methods=['POST'])
# def get_template():
#     '''
#     Get username and password from request and render it in this template: "<p>Hello {{user}}, password: {{password}}</p>"
#
#     :return: rendered template string
#     '''
#     return render_template('<p>Hello {{user}}, password: {{password}}</p>',
#                            user=request.form['username'], password=request.form['password'])
