import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    certificate = certificate.strip('\n')
    cert_splt = certificate.split('-----BEGIN CERTIFICATE-----')
    cert_splt = cert_splt[0].split('----END CERTIFICATE----')
    cert_splt = cert_splt[0].strip('\n')
    cert_bytes = cert_splt.encode('utf-8')
    cert_hash = hashlib.md5(cert_bytes)
    known_hash = known_hash.replace('\n', '')

    if cert_hash.hexdigest() == known_hash:
        return True
    else:
        return False

