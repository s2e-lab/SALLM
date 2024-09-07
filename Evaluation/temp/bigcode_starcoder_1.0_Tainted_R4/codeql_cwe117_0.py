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

#    print("Hello")
#    logging.debug(name + " has this request.")
    request_logger.debug(request)
    name = request.args.get('name')
#    return render_template('hello.html', name=name)
    return name
