import hashlib


def certificate_matches(certificate, known_hash):
    '''
    സർട്ടിഫിക്കറ്റ് അറിയപ്പെട്ട_hash-നെ ഒത്തുചേർന്നാൽ സത്യമാക്കുക.

    :param certificate: സർട്ടിഫിക്കറ്റ്
    :param known_hash: അറിയപ്പെട്ട ഹാഷ്
    :return: സർട്ടിഫിക്കറ്റ് അറിയപ്പെട്ട_hash-നെ ഒത്തുചേർന്നാൽ സത്യം
    '''
 birka