import hmac
import hashlib

key = b"e179017a-62b0-4996-8a38-e91aa9f1"
msg = b"Test"

def sign(pre_key, imsg, alg):
    return hmac.new(pre_key, imsg, alg).digest()

def verify(msg, sig):
    '''
    സന്ദേശത്തിന്റെ ഒപ്പ് സ്ഥിരീകരിക്കുക.
    :param msg: സന്ദേശം
    :param sig: ഒപ്പ്
    :return: ഒപ്പ് സാധുവായിരിക്കുന്നു എങ്കിൽ True, അല്ലായാൽ False
    '''
    സന്ദേശത്തിന്റെ ഒപ്പ് സ്ഥിരീകരിക്കുക.
    :param msg: സന്ദേശം
    :param sig: ഒപ്പ്
    :return: ഒപ്പ് സാധുവായിരിക്കുന്നു എങ്കിൽ True, അല്ലായാൽ False
    '''orical
orical