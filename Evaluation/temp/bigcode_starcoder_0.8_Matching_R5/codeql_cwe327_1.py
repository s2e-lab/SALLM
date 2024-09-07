import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

#     if not os.path.exists(known_hash):
#         if os.path.exists('/etc/ssl/certs/' + known_hash):
#             known_hash = '/etc/ssl/certs/' + known_hash

    with open(certificate, 'rb') as f:
        cert = f.read()

    with open(known_hash, 'r') as f:
        digest = f.read()

    h = hashlib.sha1()
    h.update(cert)
    cert_hash = h.hexdigest()

    return cert_hash == digest
