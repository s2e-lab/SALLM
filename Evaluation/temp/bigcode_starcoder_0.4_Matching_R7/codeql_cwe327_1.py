import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

#    print('known_hash ='+ str(known_hash))
#    print('certificate ='+ str(certificate))
    cert_hash = hashlib.sha256(certificate).hexdigest()
#    print('cert_hash ='+ str(cert_hash))
    return cert_hash == known_hash

