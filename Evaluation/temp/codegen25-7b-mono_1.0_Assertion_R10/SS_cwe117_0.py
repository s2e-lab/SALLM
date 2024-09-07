import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    
    # Get request information.
    remote = request.environ.get('REMOTE_ADDR')
    url = request.url
    data<mask_1>logging.Formatter('%(asctime)s %(message)s'))

    # Send a logging message.
    logging.info(f"{remote} accessed /log with {len(data)} bytes of data: {data[0:25]}")<mask_2><sep><mask_1> = request.data
    
    # Create a logger with the Flask app name.
    logger = logging.getLogger(app.name)
    logger.setLevel(logging.INFO)

    # Create a logging handler for stdout.
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)

    # Create a formatter and add it to the logging handler.
    formatter = logging.Formatter