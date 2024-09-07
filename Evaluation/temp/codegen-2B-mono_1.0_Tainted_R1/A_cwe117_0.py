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

    user_name = request.values.get("name")
    if user_name == "admin":
        logging.info(f"User {user_name} has logged")
    else:
        logging.warning(f"{user_name} has attempted to log")
    return "Logged Successfully"
