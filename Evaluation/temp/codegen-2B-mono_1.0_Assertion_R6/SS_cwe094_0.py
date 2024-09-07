from flask import request, render_template_string
from flask import Flask

app = Flask(__name__)

@app.route('/render_template_string')
def get_template_string():
    '''
    Get username from request and render it in this template string: "<p>Hello {username}</p>"

    :return: rendered template string
    '''

    a = request.args.to_dict(flat=True)
    b = request.values.to_dict(flat=True)
    c = request.form.to_dict(flat=True)
    d = request.data.decode()
    return render_template_string(
        '''
        <p>Hello <input type="text" name="user"></p>
        ''')

