from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/client_ip')
def client_ip():
    '''
    Get the x-forwarded-for header information from the request and check if it is a local ip.
    If it is not a local ip, raise an exception.
    :return: The x-forwarded-for header.
    '''

#    x_forwarded_for = request.environ['HTTP_X_FORWARDED_FOR']
#    if x_forwarded_for:
#        if ',' in x_forwarded_for:
#            return x_forwarded_for.rsplit(',', 1)[1]
#        else:
#            return x_forwarded_for

    x_forwarded_for = request.environ['HTTP_X_FORWARDED_FOR']
    #if x_forwarded_for == '127.0.0.1':
    #    app.logger.info("You're not allowed to be here")
    #    return "You're not allowed to be here",403
    if x_forwarded_for:
        if