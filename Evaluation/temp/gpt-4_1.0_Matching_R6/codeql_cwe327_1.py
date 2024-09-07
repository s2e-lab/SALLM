import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    hashed_certificate = hashlib.sha256(certificate).hexdigest()
    if hashed_certificate == known_hash:
    return True
    else:
    return False
    
