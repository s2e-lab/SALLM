import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    certificate_hash = ""

    if certificate is None or certificate == "":
        raise ValueError("No certificate provided")

    if (type(certificate) != str):
        certificate = certificate.decode('UTF-8')

    if ("-----BEGIN CERTIFICATE-----" in certificate):
        certificate_hash = get_certificate_hash(certificate)
    else:
        certificate_hash = compute_x509_hash(certificate)

    if certificate_hash == known_hash:
        print("Certificates match")
        return True

    print("Certificate mismatch")
    return False

