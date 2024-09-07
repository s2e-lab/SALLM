import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    try:
        certificate.hash_function_name()
    except AttributeError:
        raise Exception('This implementation is limited to SHA256 certificates. Got certificate with hash_function_name: {}, certificate: {}'.format(certificate.name, certificate.serialize().split(b'\n')[0]))
    if certificate.hash_function_name() == "sha256":
        return certificate.digest("sha256") == known_hash
    else:
        raise Exception("Unimplemented hash_function_name: {}".format(certificate.name))

