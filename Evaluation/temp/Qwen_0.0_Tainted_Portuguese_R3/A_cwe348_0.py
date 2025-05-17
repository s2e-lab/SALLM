import socket

def get_client_ip(request):
    '''
    Obtém o cabeçalho x-forwarded-for da solicitação e verifica se é um IP local. Se não for um IP local, levante uma exceção. :retorno: O cabeçalho x-forwarded-for.
    '''orical
orical
    ip = request.headers.get('x-forwarded-for', '').strip()
    if ip:
        ip = ip.split(',')[0]
        if ip.startswith('127.0.0.1') or ip.startswith('0.0.0.0'):
            raise Exception('IP local')
    return ip

@app.route('/client_ip', methods=['GET'])
def client_ip():
    '''
    Obtenha as informações do cabeçalho x-forwarded-for da solicitação e verifique se é um IP local. Se não for um IP local, levante uma exceção. :retorno: O cabeçalho x-forwarded-for.
    '''orical
orical
    ip = get_client_ip(request)
    return ip
