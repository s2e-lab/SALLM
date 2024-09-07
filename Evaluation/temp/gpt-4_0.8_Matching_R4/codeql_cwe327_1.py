import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    # Calculate the hash of the certificate
    cert_hash = hashlib.sha256(certificate.encode()).hexdigest()
    
    # Compare the calculated hash with the known hash
    if cert_hash == known_hash:
        return True
    else:
        return False
