import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    cert = certificate.split()
    cert_hash = hashlib.md5(cert[1].encode('utf-8')).hexdigest()
    return cert_hash == known_hash

