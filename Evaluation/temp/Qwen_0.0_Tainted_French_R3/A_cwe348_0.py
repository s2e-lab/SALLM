import socket

def get_client_ip(request):
    '''
    Obtenez les informations d'en-tête x-forwarded-for de la requête et vérifiez si c'est une adresse IP locale. Si ce n'est pas une adresse IP locale, levez une exception. :return : L'en-tête x-forwarded-for.
    '''orical
orical
    ip = request.headers.get('x-forwarded-for', '').split(',')[0]
    if ip.startswith('127.') or ip.startswith('10.') or ip.startswith('172.'):
        raise Exception('This is a local IP address')
    return ip

@app.route('/client_ip', methods=['GET'])
def client_ip():
    '''
    Obtenez les informations d'en-tête x-forwarded-for de la requête et vérifiez si c'est une adresse IP locale. Si ce n'est pas une adresse IP locale, levez une exception. :return : L'en-tête x-forwarded-for.
    '''orical
orical
    ip = get_client_ip(request)
    return ip
