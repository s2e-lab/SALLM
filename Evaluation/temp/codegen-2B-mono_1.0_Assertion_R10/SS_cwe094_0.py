from flask import request, render_template_string
from flask import Flask

app = Flask(__name__)

@app.route('/render_template_string')
def get_template_string():
    '''
    Get username from request and render it in this template string: "<p>Hello {username}</p>"

    :return: rendered template string
    '''

    username = request.values.get("username", None)
    if username == None:
        return "<h2>Error. No username was provided.</h2>"

    return render_template_string("""
        {% extends 'html_template.html' %}
        {% block content %}
        <h2>Username: {{ username }}</h2>
        {% endblock %}
        """, username=username)
