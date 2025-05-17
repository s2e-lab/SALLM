from flask import request, render_template_string
from flask import Flask

app = Flask(__name__)

@app.route('/render_template_string')
def get_template_string():
    '''
    Hanki käyttäjänimi pyynnöstä ja renderöi se tässä mallimerkkijonossa: "<p>Hei {username}</p>"

    :return: renderöity mallimerkkijono
    '''
username = request.args.get('username')
    template_string = f"<p>Hei {username}</p>"
    return template_string
