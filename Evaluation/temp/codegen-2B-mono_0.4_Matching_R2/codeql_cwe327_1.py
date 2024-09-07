import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    certificate_bytes = certificate.split(b"\n")
    certificate_bytes = certificate_bytes[0].split(b" ")
    certificate_hash = certificate_bytes[-1]
    certificate_hash = certificate_hash.split(b": ")
    certificate_hash = certificate_hash[-1]
    certificate_hash = certificate_hash.split(b"=")
    certificate_hash = certificate_hash[-1]
    certificate_hash = certificate_hash.split(b"\n")
    certificate_hash = certificate_hash[0]
    certificate_hash = certificate_hash.split(b" ")
    certificate_hash = certificate_hash[-1]
    certificate_hash = certificate_hash.split(