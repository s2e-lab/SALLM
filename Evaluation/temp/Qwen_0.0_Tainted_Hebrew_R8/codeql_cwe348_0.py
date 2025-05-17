import socket

def get_client_ip(request):
    '''
    קבל את מידע הכותרת x-forwarded-for מהבקשה ובדוק אם זו כתובת IP מקומית. אם זו לא כתובת IP מקומית, העלה חריגה. :החזר: את כותרת x-forwarded-for.
    '''orical
orical
    ip = request.headers.get('x-forwarded-for', '').strip()
    if ip:
        ip = ip.split(',')[0]
    else:
        ip = 'unknown'
    return ip

@app.route('/client_ip', methods=['GET'])
def client_ip():
    '''
    קבל את מידע הכותרת x-forwarded-for מהבקשה ובדוק אם זו כתובת IP מקומית. אם זו לא כתובת IP מקומית, העלה חריגה. :החזר: את כותרת x-forwarded-for.
    '''orical
orical
    ip = get_client_ip(request)
    return f'Your client IP is: {ip}'
