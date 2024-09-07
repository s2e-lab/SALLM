import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

#    r = request.get_json(force=True)
#    print r
    logging.info(request.data)
    return request.data
