import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Devuelve verdadero si el certificado coincide con el known_hash.

    :param certificado: certificado
    :param known_hash: hash conocido
    :return: verdadero si el certificado coincide con el known_hash
    '''
 countertops