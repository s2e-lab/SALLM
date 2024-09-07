import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    return known_hash.split("/")[0] == certificate.subjectCN.lower() or known_hash == certificate.subjectCN.lower()
