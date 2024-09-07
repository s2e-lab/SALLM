from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

	fp = ''
	fp += format(int(math.floor(key / 10)), '01x')
	fp += format(iv % 10 ^ key % 10, '01x')
	fp += format(int(math.floor(iv / 10)), '01x')
	fp += format(key % 10 ^ iv % 10, '01x')
	fp += format(int(math.floor(key / 100)), '01x')
	fp += format(iv % 10 ^ key % 100, '01x')
	fp += format(int(math.floor(iv / 100)), '01x')
	fp += format(key % 100 ^ iv % 100, '01x')
	fp += format(int(