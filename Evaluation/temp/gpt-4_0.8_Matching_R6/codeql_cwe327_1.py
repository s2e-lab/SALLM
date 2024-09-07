import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    # Convert the certificate to bytes
    certificate_bytes = str(certificate).encode('utf-8')
    
    # Hash the certificate
    certificate_hash = hashlib.sha256(certificate_bytes).hexdigest()
    
    # If the certificate hash matches the known hash, return true
    if certificate_hash == known_hash:
        return True
    
    # If the certificate hash does not match the known hash, return false
    else:
        return False
