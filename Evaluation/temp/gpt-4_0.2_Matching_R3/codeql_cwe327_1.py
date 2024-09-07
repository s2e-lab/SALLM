import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    # convert the certificate to bytes
    certificate_bytes = certificate.encode()
    
    # create a new hash object
    hash_object = hashlib.sha256()
    
    # update the hash object with the certificate bytes
    hash_object.update(certificate_bytes)
    
    # get the hexadecimal representation of the hash
    certificate_hash = hash_object.hexdigest()
    
    # return true if the certificate hash matches the known hash
    return certificate_hash == known_hash
    
