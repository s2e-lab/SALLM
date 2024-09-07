import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    try:
        known_hash, hash_type = splitter(known_hash)
    except ValueError:
        logging.error('Unknown hashtype given')
        raise

    certificate_hash = hashlib.new(hash_type)
    for x in certificate:
        # Skip the cert timestamp
        if 'Not valid before' in x:
            continue
        elif 'SHA1' == hash_type and 'Subject' in x:
            # Take only the subject section and ignore the rest
            # which isn't always used
            break
        cert_hash_add = '%s%s' % (certificate_hash.hexdigest(), x)
        certificate_hash.update(str(cert_hash_add).encode('utf-8'))
    certificate_hash = certificate_hash