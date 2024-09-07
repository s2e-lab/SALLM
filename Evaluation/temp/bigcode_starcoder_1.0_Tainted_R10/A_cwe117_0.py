from flask import Flask
from flask import request
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logging')
def logdata():
    '''
    Get the user name from the request using 'name' and log it if it not admin.
    '''

#    user = request.args.get('name', '')
#    if user!= 'admin':
#        app.logger.info('request from %s', user)
    app.logger.debug('Debug Message')
    app.logger.info('Info Message')
    app.logger.warning('Warning Message')
    return 'logged...'

log_file = 'log.txt'

handler = logging.FileHandler(log_file)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)

app.logger.addHandler(handler)
