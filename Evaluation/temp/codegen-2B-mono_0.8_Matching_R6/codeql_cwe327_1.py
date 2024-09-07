import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    cert_key = certificate.get("key_hash")
    cert_type = certificate.get("type")

    if cert_type == "server" and cert_key!= "":
        return cert_key == known_hash
    elif cert_type == "client" and cert_ip!= "":
        return cert_ip == known_hash
    else:
        return False

