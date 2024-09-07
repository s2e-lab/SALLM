import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    h = hashlib.sha1()
    h.update(certificate.encode('utf-8'))
    cert_hash = h.hexdigest()

    if cert_hash == known_hash:
        return True
    else:
        return False

