import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    cert_bytes<mask_1>sha256(<mask_2><sep><mask_1> = certificate.public_bytes(serialization.Encoding.PEM)
    return hashlib.<eom><mask_2>cert_bytes).hexdigest()<eom>