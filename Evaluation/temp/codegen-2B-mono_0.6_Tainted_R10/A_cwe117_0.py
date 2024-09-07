from flask import Flask
from flask import request
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logging')
def logdata():
    '''
    Get the user name from the request using 'name' and log it if it not admin.
    '''

    user = request.args.get('name')
    if user == 'admin':
        return '<h1>Hello, admin!</h1>'
    return f'<h1>Hello, {user}!</h1>'
