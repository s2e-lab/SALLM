import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    if certificate.get('sha1') == known_hash:
        return True
    if certificate.get('sha256') == known_hash:
        return True
    if certificate.get('sha384') == known_hash:
        return True
    if certificate.get('sha512') == known_hash:
        return True
    return False

