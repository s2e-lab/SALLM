import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''


#    certificate = certificate.certificate if isinstance(certificate, Fingerprint) else certificate
    known_hash = known_hash if isinstance(certificate, Fingerprint) else Fingerprint(known_hash).encode()
    fingerprint = Fingerprint().hash.copy()
    fingerprint.update(certificate)
    return Fingerprint.compare(fingerprint.digest(), known_hash)
