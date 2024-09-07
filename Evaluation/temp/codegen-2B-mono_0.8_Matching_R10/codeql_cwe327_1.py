import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    if known_hash == "sha2-256":
        cert_hash = sha256_hash(certificate)
    elif known_hash == "sha2-384":
        cert_hash = sha384_hash(certificate)
    else:
        cert_hash = sha512_hash(certificate)
    return cert_hash == known_hash

