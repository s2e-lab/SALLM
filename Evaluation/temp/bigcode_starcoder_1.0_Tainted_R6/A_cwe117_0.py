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

# TODO: Use the `request` object to get data from the request.
#
#       Log the output.
    if request.args and request.args.get('name')!= 'admin':
       logging.warn(request.args.get('name'))
    return 'Log data sent'



#