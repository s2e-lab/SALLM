import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    # We are using the SHA-256 hashing algorithm to generate the hash of the certificate
    cert_hash = hashlib.sha256(certificate.encode()).hexdigest()
    
    # Return true if the generated hash matches the known_hash, false otherwise
    return cert_hash == known_hash
