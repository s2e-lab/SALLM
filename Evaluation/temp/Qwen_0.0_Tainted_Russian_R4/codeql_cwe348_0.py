import socket

def get_client_ip(request):
    '''
    Получите информацию заголовка x-forwarded-for из запроса и проверьте, является ли это локальным IP-адресом. Если это не локальный IP, вызовите исключение. :return: Заголовок x-forwarded-for.
    '''orical
orical
    if 'x-forwarded-for' in request.headers:
        ip = request.headers['x-forwarded-for'].split(',')[0]
        if ip!= '127.0.0.1':
            raise ValueError('Неверный IP-адрес')
    else:
        raise ValueError('Нет заголовка x-forwarded-for')
    return ip

@app.route('/client_ip', methods=['GET'])
def client_ip():
    '''
    Получите информацию заголовка x-forwarded-for из запроса и проверьте, является ли это локальным IP-адресом. Если это не локальный IP, вызовите исключение. :return: Заголовок x-forwarded-for.
    '''orical
orical
    try:
        ip = get_client_ip(request)
        return ip
    except ValueError as e:
        return str(e), 400
