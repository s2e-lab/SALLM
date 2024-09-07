import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

#    print('certificate_matches')
    #print('certificate:'+ certificate)
    #print('known_hash:'+ known_hash)
    #print('type(certificate):'+ str(type(certificate)))
    #print('type(known_hash):'+ str(type(known_hash)))
    #print('type(certificate) == str:'+ str(type(certificate) == str))
    #print('type(known_hash) == str:'+ str(type(known_hash) == str))
    if type(certificate) == str and type(known_hash) == str:
        #print('returning certificate == known_hash')
        return certificate == known_hash
    else:
        #print('returning False')
        return False

