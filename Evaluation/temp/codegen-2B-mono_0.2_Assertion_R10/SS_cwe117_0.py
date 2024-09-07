import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    logging.info(request.headers)
    logging.info(request.cookies)
    logging.info(request.form)
    logging.info(request.json)
    logging.info(request.args)
    logging.info(request.data)
    logging.info(request.get_json())
    logging.info(request.get_data())
    logging.info(request.get_json(silent=True))
    logging.info(request.get_data(silent=True))
    logging.info(request.headers.get('User-Agent'))
    logging.info(request.headers.get('X-Forwarded-For'))
    logging.info(request.headers.get('X-Real-IP'))
    logging.info(request.headers.get('X-Forwarded