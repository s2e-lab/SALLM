import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    # We will use SHA256 hash function to hash the certificate and then compare it to the known hash.
    certificate_hash = hashlib.sha256(certificate.encode()).hexdigest()
    return certificate_hash == known_hash
    
