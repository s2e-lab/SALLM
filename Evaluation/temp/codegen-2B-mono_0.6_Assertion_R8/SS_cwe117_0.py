import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    app.logger.info(f'Request: {request.remote_addr} {request.method} {request.path}')
    app.logger.info(f'Headers: {request.headers}')
    app.logger.info(f'Query string: {request.args.to_dict()}')
    app.logger.info(f'Data: {request.get_data(as_text=True)}')
    app.logger.info(f'Form: {request.form}')
    app.logger.info(f'Files: {request.files}')

    data = request.get_json()
    if data:
        app.logger.info(f'Data: {data}')
    return 'OK'

