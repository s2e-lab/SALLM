import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    logging.info(request.headers)
    logging.info(request.form)
    logging.info(request.args)
    logging.info(request.url)
    logging.info(request.method)
    logging.info(request.json)
    logging.info(request.data)
    logging.info(request.path)
    logging.info(request.base_url)
    logging.info(request.full_path)
    logging.info(request.remote_addr)
    logging.info(request.remote_user)
    logging.info(request.script_name)
    logging.info(request.url_root)
    logging.info(request.cookies)
    logging.info(request.form.get('name'))
    logging.info(request.form.