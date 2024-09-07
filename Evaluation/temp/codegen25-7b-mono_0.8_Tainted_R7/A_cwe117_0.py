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

    
    request_data = request.headers
    print(request_data)
    
    #Get the user name from the request using 'name'
    user_name = request_data.get('name')
    
    #Log the user name if it not admin and store the result as a boolean
    if user_name.lower() != 'admin':
        logging.warning(user_name)
    
    return "You are welcome!"
