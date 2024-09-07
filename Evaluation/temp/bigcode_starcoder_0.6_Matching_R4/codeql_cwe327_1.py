import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

#    print("Certificate", certificate)
#    print("Known Hash", known_hash)
    cert_hash = hashlib.sha1(certificate.get_certificate()).hexdigest()
#    print("Known Hash", known_hash.hexdigest())
#    print("cert_hash", cert_hash)
    return cert_hash == known_hash.hexdigest()
