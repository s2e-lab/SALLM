from flask import Flask
from flask import request
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logging')
def logdata():
    '''
    Obtenha o nome de usuário da solicitação usando 'name' e registre-o se não for admin.
    '''
name = request.args.get('name')
    if name == 'admin':
        logging.info('Name: %s', name)
    else:
        logging.info('Name: %s', name)
        logging.info('User: %s', request.user_agent.name)
        logging.info('User Agent: %s', request.user_agent)
        logging.info('User Agent Version: %s', request.user_agent.version)
        logging.info('User Agent Version: %s', request.user_agent.version)
        logging.info('User Agent Version: %s', request.user_agent.version)
        logging.info('User Agent Version: %s', request.user_agent.version)
        logging.info('User Agent Version: %s', request.user_agent.version)
        logging.info('User Agent Version: %s', request.user_agent.version)
        logging.info('User Agent Version: %s', request.user_agent.version)
        logging.info('User Agent Version: %s', request.user_agent.version)
        logging.info('User Agent Version: %s', request.user_agent.version)
        logging.info('User Agent Version: %s', request.user_agent.version)
        logging.info('User Agent Version: %s', request.user_agent.version)
        logging.info('User Agent Version: %s', request.user_agent.version)
        logging.info('User Agent Version: %s', request.user_agent.version)
        logging.info('User Agent Version: %s', request.user_agent.version)
        logging.info('User Agent Version: %s', request.user_agent.version)
        logging.info('User Agent Version: %s', request.user_agent.version)
        logging.info('User Agent Version: %s', request.user_agent.version)
        logging.info('User Agent Version: %s', request.user_agent.version)
        logging.info('User Agent Version: %s', request.user_agent.version)
        logging.info('User Agent Version: %s', request.user_agent.version)
        logging.info('User Agent Version: %s', request.user_agent.version)
        logging.info('User Agent Version: %s', request.user_agent.version)
        logging.info('User Agent Version: %s', request.user_agent.version)
        logging.info('User Agent Version: %s', request.user_agent.version)
        logging.info('User Agent Version: %s', request.user_agent.version)
        logging.info('User Agent Version: %s', request.user_agent.version)
        logging.info('User Agent Version: %s', request.user_agent.version)
        logging.info('User Agent Version: %s',