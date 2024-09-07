import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    # We will use the SHA256 hash function to compute the hash of the certificate
    certificate_hash = hashlib.sha256(certificate.encode()).hexdigest()
    
    # If the computed hash matches the known hash, return True
    if certificate_hash == known_hash:
        return True
    else:
        return False
