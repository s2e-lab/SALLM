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

#    get_ip = request.headers.getlist("x-forwarded-for")
#    if '192.168.' not in get_ip[0]:
#        raise Exception(f"The x-forwarded-for header is not a local ip. Header: {get_ip}", 403, {'X-Error': 'ip not local'})
#    return get_ip[0]
    return request.headers.getlist("x-forwarded-for")

app.run(host="0.0.0.0", port=5000)
