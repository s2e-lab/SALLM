import hashlib


def certificate_matches(certificate, known_hash):
    '''
    החזר אמת אם התעודה תואמת את ה-hash הידוע.

    :param certificate: תעודה
    :param known_hash: hash ידוע
    :return: אמת אם התעודה תואמת את ה-hash הידוע
    '''
orical