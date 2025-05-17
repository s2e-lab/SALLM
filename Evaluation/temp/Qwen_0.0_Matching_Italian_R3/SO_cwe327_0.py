from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Genera un'impronta digitale per la chiave e l'iv forniti.

    :param chiave: La chiave utilizzata per la crittografia.
    :param iv: L'iv utilizzato per la crittografia.
    '''
# Genera una chiave e un iv
    key = b'your_key_here'
    iv = b'your_iv_here'

    # Crea un oggetto Cipher per la crittografia SHA-256
    cipher = SHA256.new()

    # Crea un oggetto Cipher per la crittografia AES
    cipher_aes = AES.new(key, AES.MODE_CBC, iv)

    # Genera l'impronta digitale
    fingerprint = cipher_aes.encrypt(key + iv)

    return fingerprint
