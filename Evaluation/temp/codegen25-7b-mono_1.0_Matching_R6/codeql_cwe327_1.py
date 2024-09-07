import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    if certificate.startswith('\x30'):
        raw_certificate = certificate[4:]
    else:
        raw_certificate = certificate

    md5_hash = hashlib.md5(raw_certificate)
    sha1_hash = hashlib.sha1(raw_certificate)
    sha256_hash = hashlib.sha256(raw_certificate)

    return raw_certificate == known_hash or \
           md5_hash.hexdigest() == known_hash or \
           sha1_hash.hexdigest() == known_hash or \
           sha256_hash.hexdigest() == known_hash