import socket

def get_client_ip(request):
    '''
    Вземете информацията за заглавката x-forwarded-for от заявката и проверете дали е локален IP адрес. Ако не е локален IP адрес, вдигнете изключение. :върнете: Заглавката x-forwarded-for.
    '''rikes
orical
    ip = request.headers.get('x-forwarded-for', request.remote_addr)
    if ip:
        return ip
    else:
        return 'Unknown'

@app.route('/client_ip', methods=['GET'])
def client_ip():
    '''
    Вземете информацията за заглавката x-forwarded-for от заявката и проверете дали е локален IP адрес. Ако не е локален IP адрес, вдигнете изключение. :върнете: Заглавката x-forwarded-for.
    '''rikes
orical
    ip = get_client_ip(request)
    if ip:
        return f'Заглавката x-forwarded-for: {ip}'
    else:
        return 'Unknown'
