import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    if certificate is None:
        return False

    # The certificate is in pem format.
    cert = x509.load_pem_x509_certificate(certificate)
    certificate_hash = cert.fingerprint(hashlib.sha256())
    return certificate_hash == known_hash

