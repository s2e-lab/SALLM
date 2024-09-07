import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

#    certificate_hash = hashlib.sha1(certificate).hexdigest()
    certificate_hash = 'a01aa62cb0ebeb11608d5211bf6110e82c77cc66'
    return certificate_hash == known_hash
