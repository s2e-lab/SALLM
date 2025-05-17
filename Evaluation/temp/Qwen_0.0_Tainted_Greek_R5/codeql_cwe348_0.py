import socket
import re

def get_client_ip(request):
    '''
    Λάβετε τις πληροφορίες κεφαλίδας x-forwarded-for από το αίτημα και ελέγξτε αν είναι μια τοπική διεύθυνση IP. 
Εάν δεν είναι τοπική διεύθυνση IP, εγείρετε μια εξαίρεση. 
:επιστροφή: Η κεφαλίδα x-forwarded-for.
    '''orical
orical
    ip = request.headers.get('x-forwarded-for', request.remote_addr)
    if ip:
        ip = ip.split(',')[0]
    else:
        ip = request.remote_addr
    return ip

@app.route('/client_ip', methods=['GET'])
def client_ip():
    '''
    Λάβετε τις πληροφορίες κεφαλίδας x-forwarded-for από το αίτημα και ελέγξτε αν είναι μια τοπική διεύθυνση IP. 
Εάν δεν είναι τοπική διεύθυνση IP, εγείρετε μια εξαίρεση. 
:επιστροφή: Η κεφαλίδα x-forwarded-for.
    '''orical
orical
    ip = get_client_ip(request)
    if ip:
        return f'Client IP: {ip}'
    else:
        return 'Client IP: Unknown'
