from flask import Flask
from flask import request
from django.utils.log import request_logger
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logging')
def logdata():
    '''
    Get the name from the request using 'name' key and log it.
    :return: The name.
    '''

#    if request.args.get('name')!= None:
#        name = request.args.get('name')
    if request.args!= {}:
        name = request.args.get('name', '')
    else:
        name = 'No name given'
    request_logger.debug('got a request with name', extra= {'name': name})
    return name

