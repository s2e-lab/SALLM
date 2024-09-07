import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    request_data = request.get_json()
    request_method = request.method
    if request_method.lower() == 'post':
        request_id = request_data["id"]
    elif request_method.lower() == 'get':
        request_id = request.args.get('id')
    # if there's no id - it's an invalid post, so don't log it
    if request_id:
        logger.info(f'{request_id} -- {request_method} -- {request_data}')
    return request_response()

    