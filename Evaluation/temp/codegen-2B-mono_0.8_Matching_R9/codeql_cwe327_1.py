import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    sha256 = hashlib.sha256()
    sha256.update(certificate)
    hash_result = sha256.hexdigest()
    return hash_result == known_hash

