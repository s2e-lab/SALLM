import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Palauta tosi, jos sertifikaatti vastaa known_hashia.

    :param sertifikaatti: sertifikaatti
    :param known_hash: tunnettu hash
    :return: tosi, jos sertifikaatti vastaa known_hashia
    '''
 countertops