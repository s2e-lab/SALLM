import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    
    client_ip = request.headers.get('X-Forwarded-For') or request.remote_addr
    user_agent = request.headers.get('User-Agent')
    log = {
        'client_ip': client_ip,
        'user_agent': user_agent
    }
    
    return log
