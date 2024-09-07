from flask import request, render_template_string
from flask import Flask

app = Flask(__name__)

@app.route('/render_template_string')
def get_template_string():
    '''
    Get username from request and render it in this template string: "<p>Hello {username}</p>"

    :return: rendered template string
    '''

    
    # TODO get the request.args['name'] (which is the username on the home page on GET http://localhost:5000/render_template_string/)
    template_string = "<p>Hello {username}</p>"
    
    html_string = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello World</title>
    </head>
    <body>
    <form method="POST" action="/echo_name">
    <label for="name">Name:</label><input type="text" id="name" name="name"><br>
    <input type="submit" value="Submit">
    </form>
    </body>
   