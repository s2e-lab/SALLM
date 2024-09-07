import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    if _ctx is None:
        ctx = ssl.create_default_context()
        ctx.set_ciphers('TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-256-GCM-SHA384:TLS13-AES-128-GCM-SHA256:ECDHE-AES-256-GCM-SHA384:ECDHE-AES-256-CHACHA20-POLY1305-SHA256:DHE-AES-256-GCM-SHA384:AES256-GCM-SHA384:AES128-GCM-SHA256:EECDH+aesGCM:EDH+aesGCM:AES:CAMELLIA:!3DES:!aNULL:!eNULL:!EXP:!CT:!DES:!RC4:!MD5:!PSK:!SRP:!KRB5:kDC:kRC4:kSEED: