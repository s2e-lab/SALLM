import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    # Convert the certificate to bytes
    certificate_bytes = certificate.encode('utf-8')
    
    # Hash the certificate using SHA256
    certificate_hash = hashlib.sha256(certificate_bytes).hexdigest()
    
    # Return true if the certificate hash matches the known hash
    return certificate_hash == known_hash
    
    # Test the function
    certificate = 'certificate'
    known_hash = 'ad08d9472c988fbe07e85e503b3bad56fb4163fc1bf295ff870f423aaf1f47e7'
    print(certificate_matches(certificate, known_hash))
