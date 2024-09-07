import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    logging.info("REQUEST ENDPOINT: %s", request.path)

    try:
        num = int(request.args.get('x', 1))
        
        response = f"the value of x is {num}"

        return response

    except Exception as e:
        logging.error(e)

        return str(e)
	