import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    # create a new hash object
    hash_obj = hashlib.sha256()
    
    # update the hash object with the certificate
    hash_obj.update(certificate.encode())
    
    # get the hexadecimal representation of the hash
    certificate_hash = hash_obj.hexdigest()
    
    # compare the hash of the certificate with the known hash
    return certificate_hash == known_hash
