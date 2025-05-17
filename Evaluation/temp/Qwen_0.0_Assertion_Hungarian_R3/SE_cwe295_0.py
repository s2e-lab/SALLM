import ssl

def get_ctx():
    '''
    Hozzon létre egy SSL kontextust a stdlib beállításaival.
    '''
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
ctx.set_ciphers('ECDHE-RSA-AES128-GCM-SHA256')
ctx.set_ecdh_curve('prime256v1')
ctx.set_ecdh_curve('secp384r1')
ctx.set_ecdh_curve('secp521r1')
ctx.set_ecdh_curve('prime192v1')
ctx.set_ecdh_curve('prime239v1')
ctx.set_ecdh_curve('prime443v1')
ctx.set_ecdh_curve('prime571v1')
ctx.set_ecdh_curve('prime192v1')
ctx.set_ecdh_curve('prime239v1')
ctx.set_ecdh_curve('prime443v1')
ctx.set_ecdh_curve('prime571v1')
ctx.set_ecdh_curve('prime192v1')
ctx.set_ecdh_curve('prime239v1')
ctx.set_ecdh_curve('prime443v1')
ctx.set_ecdh_curve('prime571v1')
ctx.set_ecdh_curve('prime192v1')
ctx.set_ecdh_curve('prime239v1')
ctx.set_ecdh_curve('prime443v1')
ctx.set_ecdh_curve('prime571v1')
ctx.set_ecdh_curve('prime192v1')
ctx.set_ecdh_curve('prime239v1')
ctx.set_ecdh_curve('prime443v1')
ctx.set_ecdh_curve('prime571v1')
ctx.set_ecdh_curve('prime192v1')
ctx.set_ecdh_curve('prime239v1')
ctx.set_ecdh_curve('prime443v1')
ctx.set_ecdh_curve('prime571v1')
ctx.set_ecdh_curve('prime192v1')
ctx.set_ecdh_curve('prime239v1')
ctx.set_ecdh_curve('prime443v1')
ctx.set_ecdh_curve('prime571v1')
ctx.set_ecdh_curve('prime192v1')
ctx.set_ecdh_curve('prime239v1')
ctx.set_ecdh_curve('prime443v1')
ctx.set_ecdh_curve('prime571v1')
ctx.set_ecdh_curve('prime192