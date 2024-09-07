import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    cert_hash = certificate['cert_hash']
    cert_hash_type = certificate['cert_hash_type']

    if known_hash['cert_hash_type'] == cert_hash_type:
        if known_hash == cert_hash:
            return True
        else:
            return False
    else:
        return False

