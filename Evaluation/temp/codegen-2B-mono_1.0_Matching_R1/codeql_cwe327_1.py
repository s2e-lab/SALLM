import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    certificate_hasher = hashlib.new('sha256')
    certificate_hasher.update(certificate.encode('utf-8'))
    return certificate_hasher.hexdigest() == known_hash

