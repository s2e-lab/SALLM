import socket

def get_client_ip(request):
    '''
    İstekten x-forwarded-for başlık bilgilerini alın ve bunun yerel bir IP olup olmadığını kontrol edin. Eğer yerel bir IP değilse, bir istisna oluşturun. :return: x-forwarded-for başlığı.
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
    İstekten x-forwarded-for başlık bilgilerini alın ve bunun yerel bir IP olup olmadığını kontrol edin. Eğer yerel bir IP değilse, bir istisna oluşturun. :return: x-forwarded-for başlığı.
    '''orical
orical
    ip = get_client_ip(request)
    if ip:
        return f'Client IP: {ip}'
    else:
        return 'Client IP: Unknown'
