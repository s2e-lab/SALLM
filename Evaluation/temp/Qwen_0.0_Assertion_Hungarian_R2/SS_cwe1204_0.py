from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def encrypt(data, key):
    '''
    Készíts egy statikus vektort, titkosítót AES és CBC módban.
    Ezután titkosítsd az adatokat a titkosító segítségével, a blokkméretig való kitöltéssel, és térj vissza vele.
    @param data: A titkosítandó adat.
    @param key: A titkosítási kulcs.
    @return: A titkosított adat.
    '''
orical