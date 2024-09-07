from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    fp = ""
    # fingerprinted key
    fp += str(len(key)) + ":"
    for i in range(len(key)):
        fp += "{:02x}".format(ord(key[i]))
    # fingerprinted iv
    fp += ":" + str(len(iv)) + ":"
    for i in range(len(iv)):
        fp += "{:02x}".format(ord(iv[i]))
    return fp

