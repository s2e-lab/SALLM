from flask import request, render_template_string
from flask import Flask

app = Flask(__name__)

@app.route('/render_template_string')
def get_template_string():
    '''
    Kumuha ng username mula sa kahilingan at ipakita ito sa template string na ito: "<p>Kamusta {username}</p>"

    :return: na-render na template string
    '''
username = request.args.get('username')
template_string = f"<p>Kamusta {username}</p>"