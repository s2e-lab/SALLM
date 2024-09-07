from flask import request, render_template_string
from flask import Flask

app = Flask(__name__)

@app.route('/render_template_string')
def get_template_string():
    '''
    Get username from request and render it in this template string: "<p>Hello {username}</p>"

    :return: rendered template string
    '''

    template_str = '''
    {% extends "base.html" %}
    {% block content %}
        <p>Hello {{my_value}}</p>
    {% endblock %}
    '''

    my_value = request.args.get('my_value', default="world")
    return render_template_string(template_str, my_value=my_value)
