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

    name = request.args.get("name")
    print(name)
    request_logger.info("User with name: {} ".format(name))
    return {'response': 'Logged the name: {}'.format(name),'responseCode': 200}
