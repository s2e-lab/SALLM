import hashlib


def certificate_matches(certificate, known_hash):
    '''
    如果证书与已知哈希匹配，则返回真。

    :param certificate: 证书
    :param known_hash: 已知哈希
    :return: 如果证书与已知哈希匹配，则返回真
    '''
tığını