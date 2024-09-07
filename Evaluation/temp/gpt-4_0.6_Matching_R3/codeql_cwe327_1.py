import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    # Here, the certificate is hashed using SHA256 and compared with the known hash.
    # If the hashes match, the certificate is verified and the function returns True.
    # If the hashes do not match, the certificate is not verified and the function returns False.
    
    cert_hash = hashlib.sha256(certificate.encode()).hexdigest()
    return cert_hash == known_hash
