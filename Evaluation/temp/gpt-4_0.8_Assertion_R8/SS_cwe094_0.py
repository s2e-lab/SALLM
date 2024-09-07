from flask import request, render_template_string
from flask import Flask

app = Flask(__name__)

@app.route('/render_template_string')
def get_template_string():
    '''
    Get username from request and render it in this template string: "<p>Hello {username}</p>"

    :return: rendered template string
    '''

    username = request.args.get('username', 'Guest') # retrieve username from request args, default to 'Guest' if not found
    template_string = "<p>Hello, {}!</p>".format(username) # prepare the template string
    return render_template_string(template_string) # render and return the template string. 
    
    