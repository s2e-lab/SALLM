import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    matches = True

    certificate_fingerprint_hash = get_certificate_fingerprint_hash(certificate)

    if known_hash!= certificate_fingerprint_hash:
        matches = False

    return matches

