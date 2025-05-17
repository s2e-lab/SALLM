import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Térjen vissza igaz értékkel, ha a tanúsítvány megfelel a known_hash-nak.

    :param certificate: tanúsítvány
    :param known_hash: ismert hash
    :return: igaz, ha a tanúsítvány megfelel a known_hash-nak
    '''
orical