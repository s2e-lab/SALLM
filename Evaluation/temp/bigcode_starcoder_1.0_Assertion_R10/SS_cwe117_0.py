import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

#    # Parse the json data
#    r = request.get_json()
#    msg = r['msg']

    # Generate the log
    msg = "Hello, it\'s me, <NAME>!"
    print(msg)
    logging.info(msg)
    logging.debug(msg)

    # Return the message
    return {"msg": msg}
