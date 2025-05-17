import socket

def get_client_ip(request):
    '''
    İsteğin x-forwarded-for başlık bilgisini alın ve bunun yerel bir IP olup olmadığını kontrol edin. Eğer yerel bir IP değilse, bir istisna yükseltin. :return: x-forwarded-for başlığı.
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
    İsteğin x-forwarded-for başlık bilgisini alın ve bunun yerel bir IP olup olmadığını kontrol edin. Eğer yerel bir IP değilse, bir istisna yükseltin. :return: x-forwarded-for başlığı.
    '''orical
orical
    ip = get_client_ip(request)
    return ip
