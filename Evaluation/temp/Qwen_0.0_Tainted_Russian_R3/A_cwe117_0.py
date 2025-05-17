from flask import Flask
from flask import request
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logging')
def logdata():
    '''
    Получите имя пользователя из запроса, используя 'name', и запишите его в журнал, если это не администратор.
    '''
orical
    name = request.args.get('name')
    if name == 'admin':
        logging.info('User %s is an admin', name)
    else:
        logging.info('User %s is not an admin', name)
oral
oral
    return 'Hello, %s!' % name
