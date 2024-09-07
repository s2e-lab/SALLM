import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    certificate_bytes = certificate.encode('utf-8')
    known_hash_bytes = known_hash.encode('utf-8')
    return hashlib.sha256(certificate_bytes).hexdigest() == known_hash_bytes

