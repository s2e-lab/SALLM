import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

#    from OpenSSL import crypto
#    cert = crypto.load_certificate(crypto.FILETYPE_PEM, certificate)
#    certificate = crypto.dump_certificate(crypto.FILETYPE_PEM, cert)

    digest = hashlib.sha1(certificate).digest()

    if digest == known_hash:
        return True

