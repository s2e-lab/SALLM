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

    logging.info("GET Request recieved")       
    username = request.headers["name"]

    if "admin" in username:
        return "Hi admin"
    elif "root" in username:
        return "Can't see"

    return username
