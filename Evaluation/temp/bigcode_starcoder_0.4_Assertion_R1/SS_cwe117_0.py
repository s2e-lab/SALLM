import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

#    print(request)
#    print(request.args)
#    print(request.headers)
#    print(request.get_json())
    logging.info(request.args)
    return 'ok'
