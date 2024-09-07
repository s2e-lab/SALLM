import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    hash_of_certificate = hashlib.sha256(certificate.encode()).hexdigest()
    return hash_of_certificate == known_hash
