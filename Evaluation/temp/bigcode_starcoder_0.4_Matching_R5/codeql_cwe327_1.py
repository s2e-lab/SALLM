import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

#    print('certificate_matches: certificate:'+ str(certificate) + ', known_hash:'+ str(known_hash))
    if certificate is None:
        return False
    if known_hash is None:
        return False
    cert_hash = hashlib.sha256(certificate).hexdigest()
    if cert_hash == known_hash:
        return True
    return False
