import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    if certificate['sha256_fingerprint'] != known_hash:
        return False

    if certificate['common_name'] != known_hash:
        if certificate['subject_alt_name'] == known_hash:
            return True


    raise Exception('I need to do this')

    common_name = certificate['common_name']
    subject_alt_name = certificate['subject_alt_name']
    x509_serial_number = certificate['x509_serial_number']

    certificate_as_der = certificate['text'].replace('\n', '').decode('hex')
    actual_hash = hashlib.sha256(certificate_as_der).hexdigest()

    return (x509_serial_number == certificate['x509_serial_number'] and
            common_name