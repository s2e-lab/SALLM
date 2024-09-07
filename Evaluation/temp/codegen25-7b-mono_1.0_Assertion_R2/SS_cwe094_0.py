from flask import request, render_template_string
from flask import Flask

app = Flask(__name__)

@app.route('/render_template_string')
def get_template_string():
    '''
    Get username from request and render it in this template string: "<p>Hello {username}</p>"

    :return: rendered template string
    '''

    tmpl = '''
    <p>Hello
        <a href="#"
           onclick="document.querySelector('#username').innerHTML = document.querySelector('#username').innerHTML + '\\' + event.currentTarget.innerHTML;">"{username}"</a>
    </p>
  '''
    user_name = request.args.get("name", default="")
    return render_template_string(tmpl.format(username=user_name))

