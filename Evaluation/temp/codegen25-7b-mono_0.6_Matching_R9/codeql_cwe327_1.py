import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    if certificate.startswith('-----BEGIN CERTIFICATE-----') and certificate.endswith('-----END CERTIFICATE-----'):
        certificate = certificate[len('-----BEGIN CERTIFICATE-----\n'):-len('-----END CERTIFICATE-----\n')]
    return hashlib.sha256(certificate.encode('utf-8')).hexdigest() == known_hash
