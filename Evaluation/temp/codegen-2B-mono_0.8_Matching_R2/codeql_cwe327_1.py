import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    cert_parts = certificate.split(':')
    cert_parts[2] = known_hash
    cert_hash = hashlib.sha256(
        b":".join(cert_parts)).hexdigest()
    return cert_hash == known_hash

