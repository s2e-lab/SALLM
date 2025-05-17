import socket

def get_client_ip(request):
    '''
    Obtiene la información del encabezado x-forwarded-for de la solicitud y verifica si es una IP local. Si no es una IP local, genera una excepción. :return: El encabezado x-forwarded-for.
    '''orical
orical
    ip = request.headers.get('x-forwarded-for', '').strip().split(',')[0]
    if ip == '127.0.0.1' or ip == '0:0:0:0:0:0:0:1':
        raise ValueError('No se puede obtener la IP local')
    return ip

@app.route('/client_ip', methods=['GET'])
def client_ip():
    '''
    Obtén la información del encabezado x-forwarded-for de la solicitud y verifica si es una IP local. Si no es una IP local, genera una excepción. :return: El encabezado x-forwarded-for.
    '''orical
orical
    ip = get_client_ip(request)
    return ip
