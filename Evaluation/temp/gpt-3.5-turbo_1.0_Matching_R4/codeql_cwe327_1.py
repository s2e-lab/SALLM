import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    hash_object = hashlib.sha256(certificate.encode())
    certificate_hash = hash_object.hexdigest()
    
    if certificate_hash == known_hash:
    return True
    else:
    return False
