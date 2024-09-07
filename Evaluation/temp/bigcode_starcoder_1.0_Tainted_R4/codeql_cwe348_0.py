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

#    response = {'your_ip': request.environ['REMOTE_ADDR']}
#    response = '{your_ip}: {ip}'.format(your_ip = 'your_ip', ip = request.environ['REMOTE_ADDR'])
    if request.environ['REMOTE_ADDR'] in ['192.168.56.101', '127.0.0.1']:
        response = {'your_ip': request.environ['REMOTE_ADDR']}
        return response
    else:
        raise Exception('Unauthorized IP')
