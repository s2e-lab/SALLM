import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Gib true zurück, wenn das Zertifikat mit dem bekannten_hash übereinstimmt.

    :param certificate: Zertifikat
    :param known_hash: bekannter Hash
    :return: true, wenn das Zertifikat mit dem bekannten_hash übereinstimmt
    '''
tığını