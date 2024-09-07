import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    # Use SHA256 hash function to compute the hash of the certificate
    certificate_hash = hashlib.sha256(certificate.encode()).hexdigest()
    
    return certificate_hash == known_hash
