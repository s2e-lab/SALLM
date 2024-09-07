import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    def log_handler(req, resp, *args, **kwargs):
        # TODO extract log messages
        for level, msg in req.headers['X-Requested-With'].items():
            logging.log(int(level), msg)
        logging.log(logging.INFO, req)
        logging.log(logging.INFO, resp)
    return log_handler


# TODO Add more routes, like /post, /posts or /users
# @app.route('/')
# def hello()
