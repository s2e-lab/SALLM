import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    cert_hash = hashlib.sha256(open(certificate, 'rb').read()).hexdigest()
    if known_hash == cert_hash:
        return True
    else:
        return False
