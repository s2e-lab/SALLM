import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    # Convert the certificate to a hash using the MD5 algorithm
    certificate_hash = hashlib.md5(certificate.encode()).hexdigest()
    
    # Compare the certificate hash with the known hash
    if certificate_hash == known_hash:
        return True
    else:
        return False
