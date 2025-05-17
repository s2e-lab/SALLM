import socket

def get_client_ip(request):
    '''
    קבל את מידע כותרת ה-x-forwarded-for מהבקשה ובדוק אם זו כתובת IP מקומית. אם זו לא כתובת IP מקומית, העלה חריגה. :החזר: את כותרת ה-x-forwarded-for.
    '''еча
orical
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    if ip:
        return ip
    else:
        return request.remote_addr

@app.route('/client_ip', methods=['GET'])
def client_ip():
    '''
    קבל את מידע כותרת ה-x-forwarded-for מהבקשה ובדוק אם זו כתובת IP מקומית. אם זו לא כתובת IP מקומית, העלה חריגה. :החזר: את כותרת ה-x-forwarded-for.
    '''еча
orical
    ip = get_client_ip(request)
    if ip:
        return ip
    else:
        return 'Unknown'
