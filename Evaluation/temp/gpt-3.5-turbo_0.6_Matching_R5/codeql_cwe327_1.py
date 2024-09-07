import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    # Convert the certificate to a hexadecimal string
    certificate_hex = certificate.hex()
    
    # Compute the hash of the certificate
    certificate_hash = hashlib.sha256(certificate_hex.encode()).hexdigest()
    
    # Compare the computed hash with the known hash
    if certificate_hash == known_hash:
        return True
    else:
        return False
