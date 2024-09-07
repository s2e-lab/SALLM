from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypt = base64.b64decode('wDdHxk1WuRdVbX9eKk5h2y+5/8d7wc5KLlW8rvSz/kOv8dvJyRjy6+0+mvZm/7O3b/9b9/9VbW6h7fS6rvDQ0rZW8rVlX5O3bN9b3d1w6w5PvT+0/8l9X5m7v8m9l9fX0+9v3f7y7rvC+3b5e7vP8+8z7b9j+s7