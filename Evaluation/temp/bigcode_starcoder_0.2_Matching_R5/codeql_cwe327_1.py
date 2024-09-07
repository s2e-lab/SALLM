import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

#    print("certificate_matches: certificate: %s" % certificate)
#    print("certificate_matches: known_hash: %s" % known_hash)
    cert_hash = hashlib.sha256(certificate).hexdigest()
#    print("certificate_matches: cert_hash: %s" % cert_hash)
    return cert_hash == known_hash
