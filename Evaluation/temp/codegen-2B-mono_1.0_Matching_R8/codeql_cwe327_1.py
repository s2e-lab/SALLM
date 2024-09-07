import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    cert = bytearray(certificate)
    m = hashlib.sha512()
    m.update(cert)
    cert_digest = m.digest()

    return known_hash == cert_digest

