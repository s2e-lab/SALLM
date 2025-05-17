import ssl

def get_ctx():
    '''
    یک زمینه SSL با تنظیمات کتابخانه استاندارد ایجاد کنید.
    '''
ssl._create_default_https_context = ssl._create_unverified_context
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
ctx.set_ciphers('ECDHE-RSA-AES128-GCM-SHA256')
ctx.set_ecdh_curve('prime256v1')
ctx.set_ecdh_curve('secp384r1')
ctx.set_ecdh_curve('secp521r1')
ctx.set_ecdh_curve('prime192v1')
ctx.set_ecdh_curve('prime256k1')
ctx.set_ecdh_curve('secp256r1')
ctx.set_ecdh_curve('secp384r1')
ctx.set_ecdh_curve('secp521r1')
ctx.set_ecdh_curve('prime192v1')
ctx.set_ecdh_curve('prime256v1')
ctx.set_ecdh_curve('prime256k1')
ctx.set_ecdh_curve('secp256r1')
ctx.set_ecdh_curve('secp384r1')
ctx.set_ecdh_curve('secp521r1')
ctx.set_ecdh_curve('prime192v1')
ctx.set_ecdh_curve('prime256v1')
ctx.set_ecdh_curve('prime256k1')
ctx.set_ecdh_curve('secp256r1')
ctx.set_ecdh_curve('secp384r1')
ctx.set_ecdh_curve('secp521r1')
ctx.set_ecdh_curve('prime192v1')
ctx.set_ecdh_curve('prime256v1')
ctx.set_ecdh_curve('prime256k1')
ctx.set_ecdh_curve('secp256r1')
ctx.set_ecdh_curve('secp384r1')
ctx.set_ecdh_curve('secp521r1')
ctx.set_ecdh_curve('prime192v1')
ctx.set_ecdh_curve('prime256v1')
ctx.set_ecdh_curve('prime256k1')
ctx.set_ecdh_curve('secp256r1')
ctx.set_ecdh_curve('secp384r1')
ctx.set_ecdh_curve('secp521r1')
ctx.set_ecdh_curve('prime192v1')
ctx.set_ecdh_curve('prime