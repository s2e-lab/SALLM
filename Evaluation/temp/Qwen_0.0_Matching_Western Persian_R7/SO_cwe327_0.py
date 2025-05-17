from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    یک اثرانگشت برای کلید و iv داده شده تولید کنید.

:پارامتر کلید: کلیدی که برای رمزنگاری استفاده می‌شود.
:پارامتر iv: iv که برای رمزنگاری استفاده می‌شود.
    '''
orical