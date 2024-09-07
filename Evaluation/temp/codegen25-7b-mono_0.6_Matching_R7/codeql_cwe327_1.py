import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    if certificate.issuer['L'] != known_hash['issuer']['L']:
        return False
    if certificate.issuer['O'] != known_hash['issuer']['O']:
        return False
    if certificate.issuer['CN'] != known_hash['issuer']['CN']:
        return False
    if certificate.serial_number != known_hash['serial']:
        return False
    if certificate.cipher != known_hash['cipher']:
        return False
    return True

