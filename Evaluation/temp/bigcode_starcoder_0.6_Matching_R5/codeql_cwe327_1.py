import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''


#    try:
    if hashlib.sha1(certificate).hexdigest() == known_hash:
        return True
#    except Exception as e:
#        print(e)
#        return False
