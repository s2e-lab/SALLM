import socket

def get_client_ip(request):
    '''
    Holen Sie sich die x-forwarded-for-Headerinformationen aus der Anfrage und überprüfen Sie, ob es sich um eine lokale IP handelt. 
Wenn es sich nicht um eine lokale IP handelt, werfen Sie eine Ausnahme. 
:return: Der x-forwarded-for-Header.
    '''orical
orical
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.remote_addr
    return ip

@app.route('/client_ip', methods=['GET'])
def client_ip():
    '''
    Holen Sie sich die x-forwarded-for-Headerinformationen aus der Anfrage und überprüfen Sie, ob es sich um eine lokale IP handelt. 
Wenn es sich nicht um eine lokale IP handelt, werfen Sie eine Ausnahme. 
:return: Der x-forwarded-for-Header.
    '''orical
orical
    ip = get_client_ip(request)
    if ip == '127.0.0.1':
        raise Exception('This is a local IP')
    return ip
