import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

#     print('cert hash:', certificate.public_bytes(serialization.Encoding.PEM).hex())
    certificate_hash = hashlib.sha1(certificate.public_bytes(serialization.Encoding.PEM)).digest()
    known_hash_bytes = bytes.fromhex(known_hash)
#     print('known:', known_hash_bytes.hex())

    return known_hash_bytes == certificate_hash
