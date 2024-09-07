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

    logging.info('name')
    logging.debug('not admin')
    return 'nothing to see here'

# The logging.basicConfig() method is used and the level is set to 20
app.run(debug=True)

# The log data will look like this