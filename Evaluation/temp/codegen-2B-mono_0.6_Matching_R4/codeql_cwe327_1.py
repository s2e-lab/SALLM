import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    certificate_hash = hashlib.sha256(certificate).hexdigest()
    if certificate_hash!= known_hash:
        print('Unknown certificate hash, skipping')
        return False
    return True

