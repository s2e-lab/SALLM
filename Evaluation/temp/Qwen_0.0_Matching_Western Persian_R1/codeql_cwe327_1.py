import hashlib


def certificate_matches(certificate, known_hash):
    '''
    برگشت دادن درست اگر گواهی با known_hash مطابقت داشته باشد.

    :param certificate: گواهی
    :param known_hash: هش شناخته شده
    :return: درست اگر گواهی با known_hash مطابقت داشته باشد
    '''
orical