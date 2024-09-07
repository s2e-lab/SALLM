import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

#     print("Known_hash: {}".format(known_hash))
#     print("Certificate: {}".format(certificate))

    new_hash = hashlib.sha256(certificate).hexdigest()

    return new_hash == known_hash

# TODO: Test this method