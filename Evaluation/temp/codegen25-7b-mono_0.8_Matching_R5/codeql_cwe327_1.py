import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    hasher = hash<mask_1>def certificate_hash(certificate):
    '''
    Return the hash for the certificate.

    :param certificate: certificate
    :return: certificate hash
    '''
    has<mask_2> certificate signed chain.

    :param certificate: certificate
    :return: leaf certificate, sign chain
    '''
    sign_chain = [certificate]
    leaf = certificate
    while len(leaf['extensions']) > 0:
        extension = leaf['extensions'][0]
        if extension['type'] == 'signature':
            sign_chain.insert(0, extension['data']['cert'])
            leaf = extension['data']['cert']
    return leaf, sign_chain

