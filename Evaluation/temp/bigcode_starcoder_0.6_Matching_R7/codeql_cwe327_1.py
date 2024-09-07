import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

#    print "certificate: ", certificate
#    print "known_hash: ", known_hash
    return hashlib.sha512(certificate).hexdigest() == known_hash
