import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

#    print "Hashing certificate %s" % certificate
    certificate_hash = hashlib.sha512(certificate).hexdigest()
#    print "Hash: %s" % certificate_hash
    if certificate_hash == known_hash:
        return True
    else:
        return False
