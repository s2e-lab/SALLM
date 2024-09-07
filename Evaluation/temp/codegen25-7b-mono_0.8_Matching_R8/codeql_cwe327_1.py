import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    # We first check which type of certificate it is.
    first_byte = ord(certificate[0])
    if first_byte & 0x40:
        # PGP
        certificate_type_code = 1
    elif first_byte & 0x80:
        # RSA
        certificate_type_code = 2
    elif first_byte & 0xC0:
        # DSA
        certificate_type_code = 3
    else:
        # Elgamal
        certificate_type_code = 4
    # The next byte is the length of the certificate.
    len_cert = ord(certificate[1])
    # Next 4 bytes are the MD5 hash of the certificate
    md5 = certificate[2:6]
    # Next 2 bytes are the type of the certificate
