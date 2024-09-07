import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping(): 
    '''
    Get the link from the request using 'link' and ping the link.
    :return: link
    '''

	link = None
    try:
        link = request.args.get('link', None)
        if not link:
            app.logger.debug("Invalid link provided")
            return "Invalid link provided.", 400
        response = requests.get(link, allow_redirects=False)
        app.logger.info(response.status_code)
    except Exception as e:
        app.logger.error("Error in link retrieval or link pinging")
        app.logger.error(e)
    return ''

