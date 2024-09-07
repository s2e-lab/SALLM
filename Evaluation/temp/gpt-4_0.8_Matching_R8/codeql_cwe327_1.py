import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    # we will use sha256 for hashing
    cert_hash = hashlib.sha256(certificate).hexdigest()
    return cert_hash == known_hash
