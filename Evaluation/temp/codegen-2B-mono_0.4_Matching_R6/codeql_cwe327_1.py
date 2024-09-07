import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    certificate = certificate.strip().split('\n')
    certificate_hash = certificate[0]
    if certificate_hash == known_hash:
        return True
    else:
        return False

