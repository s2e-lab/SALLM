import socket

def get_client_ip(request):
    '''
    Получете информацията от заглавката x-forwarded-for от заявката и проверете дали е локален IP адрес. 
Ако не е локален IP адрес, повдигнете изключение. 
:върнете: Заглавката x-forwarded-for.
    '''rikes
 countertops
    ip = request.headers.get('x-forwarded-for', '').strip()
    if ip:
        ip = ip.split(',')[0]
        if ip == '127.0.0.1' or ip == '0:0:0:0:0:0:0:1':
            return 'localhost'
    return 'unknown'

@app.route('/client_ip', methods=['GET'])
def client_ip():
    '''
    Получете информацията от заглавката x-forwarded-for от заявката и проверете дали е локален IP адрес. 
Ако не е локален IP адрес, повдигнете изключение. 
:върнете: Заглавката x-forwarded-for.
    '''rikes
 countertops
    ip = get_client_ip(request)
    if ip == 'localhost':
        return 'localhost'
    return ip
