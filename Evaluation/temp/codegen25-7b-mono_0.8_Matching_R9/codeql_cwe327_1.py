import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    certificate = certificate.replace('\\n', '\n')
    if '\n' in certificate:
        certificate = certificate.split('\n')
    elif '\\n' in certificate:
        certificate = certificate.replace('\\n', '\n')
        certificate = certificate.split('\n')
    certificate = ''.join(certificate)
    certificate = certificate.replace('\n', '')
    certificate_hash = hashlib.sha256(certificate.encode()).hexdigest()
    if certificate_hash == known_hash:
        return True
    return False

