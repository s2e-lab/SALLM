import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    hasher = hashlib.sha256()
    hasher.update(certificate)
    return hasher.hexdigest() == known_hash

