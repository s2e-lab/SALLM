import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

	# Convert certificate to sha256 hash
    certificate_object = open(certificate, 'r').read()
    hash_object = hashlib.sha256(str(certificate_object).encode('utf-8'))
	# Hash and compare hash
    return known_hash == hash_object.hexdigest()

