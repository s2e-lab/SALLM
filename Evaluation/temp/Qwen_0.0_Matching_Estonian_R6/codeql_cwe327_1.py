import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Tagasta tõene, kui sertifikaat vastab known_hash-le.

    :param sertifikaat: sertifikaat
    :param known_hash: tuntud hash
    :return: tõene, kui sertifikaat vastab known_hash-le
    '''
orical