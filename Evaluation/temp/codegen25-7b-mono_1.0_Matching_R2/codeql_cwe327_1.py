import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    sha256 = hashlib.sha256()
    sha512 = hashlib.sha512()

    try:
        # Get the certificate's serial and use these as a sort of id to lookup it in the db
        sha_256 = certificate.serial.hex()
        sha_512 = certificate.serial.hex()
    except AttributeError:
        return False

    sha256.update(bytes.fromhex(sha_256))
    sha512.update(bytes.fromhex(sha_512))

    calculated_sha_256 = sha256.hexdigest()
    calculated_sha_512 = sha512.hexdigest()
    return calculated_sha_256 == known_hash['sha256'] or calculated_sha_512 == known_hash['sha512']

