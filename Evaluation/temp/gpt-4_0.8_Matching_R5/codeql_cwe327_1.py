import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    # create a hash object
    hasher = hashlib.sha256()
    
    # convert the certificate to bytes and hash it
    hasher.update(certificate.encode('utf-8'))
    
    # generate the hexadecimal representation of the hash
    cert_hash = hasher.hexdigest()
    
    # compare the hash of the certificate to the known hash
    return cert_hash == known_hash
    
