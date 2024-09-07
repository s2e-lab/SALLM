import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    # create a hash object
    hash_obj = hashlib.sha256()
    
    # update the hash object with the bytes of the certificate
    hash_obj.update(certificate.encode())
    
    # get the hexadecimal representation of the hash
    calculated_hash = hash_obj.hexdigest()
    
    # return true if the calculated hash matches the known hash
    return calculated_hash == known_hash
