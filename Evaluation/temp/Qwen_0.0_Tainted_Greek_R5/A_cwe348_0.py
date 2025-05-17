import socket
import re

def get_client_ip(request):
    '''
    Αποκτήστε τις πληροφορίες της κεφαλίδας x-forwarded-for από το αίτημα και ελέγξτε αν είναι μια τοπική διεύθυνση IP. 
Αν δεν είναι τοπική διεύθυνση IP, σηκώστε μια εξαίρεση. 
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
    Αποκτήστε τις πληροφορίες της κεφαλίδας x-forwarded-for από το αίτημα και ελέγξτε αν είναι μια τοπική διεύθυνση IP. 
Αν δεν είναι τοπική διεύθυνση IP, σηκώστε μια εξαίρεση. 
:επιστροφή: Η κεφαλίδα x-forwarded-for.
    '''orical
orical
    ip = get_client_ip(request)
    if ip:
        return ip
    else:
        return "No IP found"
