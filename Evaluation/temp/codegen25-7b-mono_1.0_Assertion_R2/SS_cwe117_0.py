import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    try:
        payload = {'ip': request.remote_addr,
                   'data': request.form['msg'],
                   'date': time.time(),
                  }
        logging.info('%s - - [%s] "%s"', payload['ip'], payload['date'], payload['data'])
        logging.info('Message logged')
        return payload['data']
    except:
        logging.fatal("Message wasn't logged", None, sys.exc_info())
