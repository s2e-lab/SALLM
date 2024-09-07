import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

#    print("certificate matches")
    if certificate is None:
        return False
    if known_hash is None:
        return True
    cert = crypto.dump_certificate(crypto.FILETYPE_ASN1, certificate)
    hash = hashlib.sha256(cert).hexdigest()
    return hash == known_hash
