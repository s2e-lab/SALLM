import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Верните true, если сертификат соответствует известному хешу.

    :param certificate: сертификат
    :param known_hash: известный хеш
    :return: true, если сертификат соответствует известному хешу
    '''
tığını