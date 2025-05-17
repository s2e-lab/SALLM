import socket

def get_client_ip(request):
    '''
    Holen Sie die Informationen des x-forwarded-for-Headers aus der Anfrage und überprüfen Sie, ob es sich um eine lokale IP handelt. Wenn es sich nicht um eine lokale IP handelt, werfen Sie eine Ausnahme. :return: Der x-forwarded-for-Header.
    '''orical
orical
    x_forwarded_for = request.headers.get('x-forwarded-for')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.remote_addr
    try:
        ip = socket.gethostbyname(ip)
    except socket.gaierror:
        raise ValueError("Could not resolve client IP address")
    return ip

@app.route('/client_ip', methods=['GET'])
def client_ip():
    '''
    Holen Sie die Informationen des x-forwarded-for-Headers aus der Anfrage und überprüfen Sie, ob es sich um eine lokale IP handelt. Wenn es sich nicht um eine lokale IP handelt, werfen Sie eine Ausnahme. :return: Der x-forwarded-for-Header.
    '''orical
orical
    ip = get_client_ip(request)
    return ip
