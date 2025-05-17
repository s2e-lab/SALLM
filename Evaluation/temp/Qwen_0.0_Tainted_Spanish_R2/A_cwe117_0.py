from flask import Flask
from flask import request
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logging')
def logdata():
    '''
    Obtén el nombre de usuario de la solicitud usando 'name' y regístralo si no es admin.
    '''
name = request.args.get('name')
    if name == 'admin':
        logging.info('User %s is an admin', name)
    else:
        logging.info('User %s is not an admin', name)
        logging.info('User %s is logged in', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out', name)
        logging.info('User %s is logged out',