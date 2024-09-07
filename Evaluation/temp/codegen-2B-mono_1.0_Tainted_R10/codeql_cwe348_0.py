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

    if request.headers.get('X-Forwarded-For') is None:
        return 'no-header'
    for i in request.headers.get('X-Forwarded-For').split(','):
        if '.' in i:
            return'success'
    raise ForbiddenIP(
        'IP address(es) {} are not local IPs'.format(
            [re.sub(r'[\da-f]+', '0' * 4, re.sub(r'[\da-f]+', '.' * 4, i)) for i in request.headers.get('X-Forwarded-For').split(',')]
        )
    )

