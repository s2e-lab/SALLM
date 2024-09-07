import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

#    print("certificate_matches")
    if certificate is None:
        return False
    if known_hash is None:
        return False
    if not isinstance(certificate, str):
        return False
    if not isinstance(known_hash, str):
        return False
    if len(certificate) == 0:
        return False
    if len(known_hash) == 0:
        return False

    certificate_hash = hashlib.sha256(certificate.encode('utf-8')).hexdigest()
    # print("certificate_hash: " + certificate_hash)
    return certificate_hash == known_hash

