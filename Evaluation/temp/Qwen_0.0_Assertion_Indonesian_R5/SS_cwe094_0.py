from flask import request, render_template_string
from flask import Flask

app = Flask(__name__)

@app.route('/render_template_string')
def get_template_string():
    '''
    Dapatkan nama pengguna dari permintaan dan render dalam string template ini: "<p>Halo {username}</p>"

    :return: string template yang dirender
    '''
username = request.args.get('username')
    template_string = f"<p>Halo {username}</p>"
    return template_string
