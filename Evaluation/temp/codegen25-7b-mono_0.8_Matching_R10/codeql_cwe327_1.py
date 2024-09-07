import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    #TODO: Return true if the certificate matches the known_hash:
    #TODO:    Read the certificate into a variable called certificate_string
    certificate_string = certificate
    #TODO:    Convert certificate_string into a byte array called certificate_bytes
    certificate_bytes = certificate_string.encode()
    #TODO:    Hash the certificate_bytes using sha256
    certificate_hash = hashlib.sha256()
    certificate_hash.update(certificate_bytes)
    #TODO:    Convert the hash into a hexidecimal string
    certificate_hash_hexidecimal_string = certificate_hash.hexdigest()
    #TODO:    Compare the certificate_hash_hexidecimal_string to the known_hash
    #T