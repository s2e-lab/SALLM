import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    # Convert the certificate to a hash using the MD5 algorithm
    md5_hash = hashlib.md5(certificate).hexdigest()
    
    # Compare the hash of the certificate to the known hash
    if md5_hash == known_hash:
        return True
    else:
        return False
