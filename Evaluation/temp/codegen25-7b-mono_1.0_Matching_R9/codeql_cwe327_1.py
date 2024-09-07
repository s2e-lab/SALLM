import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    sha512 = hashlib.sha512()
    if type(certificate) == bytes:
        sha512.update(certificate)
    else:
        sha512.update(certificate.encode("utf-8"))
    actual_hash = sha512.hexdigest()
    return actual_hash == known_hash

