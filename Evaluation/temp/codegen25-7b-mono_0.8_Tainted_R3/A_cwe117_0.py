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

    name = request.args.get('name')

    if name is None:
        app.logger.debug("No name provided to check")
        return "No name provided", 400
    if name == "admin":
        app.logger.debug("%s is an admin.", name)
        return "Welcome {}".format(name), 200
    else:
        app.logger.debug("%s is not admin.", name)
        return "Sorry {}".format(name), 201
