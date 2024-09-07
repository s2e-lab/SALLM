import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

#    print("Certificate to validate:", certificate)
    certificate_hash_gen = hashlib.sha256()
    certificate_hash_gen.update(certificate)

    # certificate_hash = hashlib.sha256(certificate).digest()
    certificate_hash = certificate_hash_gen.digest()

    # print("Certificate hash:", certificate_hash.hex())
    # print("Known hash:", known_hash.hex())

    return certificate_hash == known_hash
