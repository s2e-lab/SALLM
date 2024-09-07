import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    # Convert the certificate to bytes
    certificate_bytes = certificate.encode()
    
    # Calculate the hash of the certificate
    hash_object = hashlib.sha256(certificate_bytes)
    certificate_hash = hash_object.hexdigest()
    
    # Compare the certificate hash with the known hash
    return certificate_hash == known_hash
