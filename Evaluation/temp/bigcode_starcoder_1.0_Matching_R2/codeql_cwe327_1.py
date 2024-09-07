import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

#     if isinstance(certificate, six.string_types) and not IS_PY3:  # noqa: F821
#         certificate_bytes = certificate
#     else:
    certificate_bytes = certificate.public_bytes(serialization.Encoding.PEM)

    certificate_hash = hashlib.sha256(certificate_bytes).hexdigest()
    return (certificate_hash == known_hash)
