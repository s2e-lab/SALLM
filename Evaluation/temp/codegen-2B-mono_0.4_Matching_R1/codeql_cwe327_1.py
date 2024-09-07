import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    cert_hash = hashlib.sha256()
    cert_hash.update(certificate)
    cert_hash = cert_hash.hexdigest()
    return cert_hash == known_hash

