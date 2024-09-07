import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    try:
        if certificate['certType'] == 'STANDARD':  # not signed by root CA
            cert = x509.Certificate.load(certificate['certificate'])
            subject = cert._subject
            common_name = subject.rfc4514_string()
            if common_name!= 'rootCA Signed Certificate':  # 'rootCA Signed Certificate' certificate is special and for our own use
                known_hash = hashlib.sha256(known_hash).digest()
                if certificate['cert'] == known_hash:
                    return True
        elif certificate['certType'] == 'CRL':  # not signed by root CA
            if certificate['certID']!= '':  # this is a self-signed certificate
                known_hash = hashlib.sha256(known_hash