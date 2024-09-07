import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    # Calculate the hash of the certificate using the same method used to generate the known_hash
    calculated_hash = hashlib.sha256(certificate.encode()).hexdigest()
    
    # Check if the calculated hash matches the known_hash
    return calculated_hash == known_hash
