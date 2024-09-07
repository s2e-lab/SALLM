import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''


#    print("certificate_matches: certificate: " + certificate)
#    print("certificate_matches: known_hash: " + known_hash)

    if certificate is None:
        return False
    if known_hash is None:
        return False

    certificate_hash = hashlib.sha256(certificate).hexdigest()
    return certificate_hash == known_hash
