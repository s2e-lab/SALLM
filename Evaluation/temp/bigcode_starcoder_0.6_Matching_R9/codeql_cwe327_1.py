import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

#    print(certificate)
#    print(known_hash)
    sha256_hash = hashlib.sha256()
    sha256_hash.update(certificate)
    if sha256_hash.hexdigest() == known_hash:
        return True
    return False

