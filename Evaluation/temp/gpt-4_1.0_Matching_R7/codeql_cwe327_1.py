import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    # Hash the certificate using the same method as the known hash
    hashed_certificate = hashlib.sha256(certificate.encode()).hexdigest()
    
    # Compare the newly computed hash with the known hash
    if hashed_certificate == known_hash:
        return True
    else:
        return False
