import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

#     print(certificate)
#     print(known_hash)
    cert_der = crypto.dump_certificate(crypto.FILETYPE_ASN1, certificate)
    sha256 = hashlib.sha256(cert_der).digest()
    known_hash = known_hash.encode()
    return sha256 == known_hash

