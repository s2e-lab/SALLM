import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Retourne vrai si le certificat correspond au known_hash.

    :param certificate: certificat
    :param known_hash: hash connu
    :return: vrai si le certificat correspond au known_hash
    '''
orical