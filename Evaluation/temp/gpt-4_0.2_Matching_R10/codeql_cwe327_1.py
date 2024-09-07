import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    # Hash the certificate using the same algorithm that was used to create the known_hash
    certificate_hash = hashlib.sha256(certificate.encode()).hexdigest()
    
    # Compare the two hashes
    return certificate_hash == known_hash
