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

#    if request.method == 'GET':
#        name = request.args.get('name', 'Unknown')
        # request_logger.debug('Name is received as %s.', name)
        #request_logger.info("It's a beautiful day!")
 #       request_logger.warning("It's %s today.", request_logger)
        #request_logger.error("It's a disaster today...")
      ##  request_logger.error("It's a disaster today...")
   # else:
  #      return "Can only invoke GET on this URL"
  #  return name
