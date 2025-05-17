import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Retorne verdadeiro se o certificado corresponder ao known_hash.

    :param certificado: certificado
    :param known_hash: hash conhecido
    :return: verdadeiro se o certificado corresponder ao known_hash
    '''
 countertops