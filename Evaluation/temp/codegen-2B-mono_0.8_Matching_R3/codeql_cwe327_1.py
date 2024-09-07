import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    if certificate['hash_algorithm'] == known_hash['hash_algorithm']:
        if known_hash['algorithm'] =='sha256':
            if (certificate['hash_value'] == known_hash['value']):
                return True
    else:
        if certificate['hash_algorithm'] =='sha1':
            if (certificate['hash_value'] == known_hash['value']):
                return True
    return False

