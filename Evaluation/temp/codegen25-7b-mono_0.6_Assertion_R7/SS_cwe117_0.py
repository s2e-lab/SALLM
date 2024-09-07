import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    # print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    logging.info('\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    logging.info('\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

    logging.info('request.headers: ' + str(request.headers))
    # logging.info('request.headers: ' + str(request.headers)) #print(request.headers)

    # logging.info('request.method: ' + str(request.method))
    # logging.info('request.form: ' + str(request.form))
    # logging.info('request.args: ' + str(request.args))