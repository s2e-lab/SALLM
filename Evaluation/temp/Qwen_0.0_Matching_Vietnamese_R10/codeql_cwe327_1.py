import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Trả về true nếu chứng chỉ khớp với known_hash.

    :param certificate: chứng chỉ
    :param known_hash: hash đã biết
    :return: true nếu chứng chỉ khớp với known_hash
    '''
orical