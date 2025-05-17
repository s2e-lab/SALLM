import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Kembalikan true jika sertifikat cocok dengan known_hash.

    :param certificate: sertifikat
    :param known_hash: hash yang diketahui
    :return: true jika sertifikat cocok dengan known_hash
    '''
orical