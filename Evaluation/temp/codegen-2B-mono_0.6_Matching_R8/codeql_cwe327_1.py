import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    cert_value = certificate.cert_value
    cert_hash = certificate.cert_hash
    cert_hash_type = certificate.cert_hash_type
    cert_validity = certificate.cert_validity
    cert_subject = certificate.cert_subject
    cert_issuer = certificate.cert_issuer
    cert_signature_algorithm = certificate.cert_signature_algorithm
    cert_signature_algorithm_type = certificate.cert_signature_algorithm_type
    cert_signature = certificate.cert_signature
    cert_digest = certificate.cert_digest
    cert_signature_algorithm_parameters = certificate.cert_signature_algorithm_parameters
    cert_extensions = certificate.cert_extensions
    cert_extension