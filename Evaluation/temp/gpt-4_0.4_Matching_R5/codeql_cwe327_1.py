import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    # calculate the hash of the certificate
    calculated_hash = hashlib.sha256(certificate.encode()).hexdigest()
    
    # compare the calculated hash with the known hash
    return calculated_hash == known_hash
