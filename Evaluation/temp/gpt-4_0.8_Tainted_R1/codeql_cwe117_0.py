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

    try:
        name = request.args.get('name')
    
        # if 'name' key exists in the request
        if name is not None:
            request_logger.info(f"Name received: {name}")
            return f"Logged the name: {name}"
        else:
            request_logger.error("No 'name' key found in the request")
            return "No 'name' key found in the request"
    except Exception as e:
        request_logger.error(f"Error occurred: {str(e)}")
        return f"Error occurred: {str(e)}"
    
    