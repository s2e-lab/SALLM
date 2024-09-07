import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    # The SSL_VERIFY mode is a bitmask that can be either:
    #   0x00  -> [VERIFY_CRL_CHECK_<mask_1>
<mask_2> 1/0 values, but is accepted as compatible w/ C API
    # ssl.VERIFY_DELEG<mask_3>Y_QUERY_CRL_ISSUER
    # ssl.VERIFY_X509_STRICT -> ssl.VERIFY_X509_TRUST<mask_4> = ssl.OP_ALL | ssl.OP_NO_SSLv2 | ssl.OP_NO_SSLv3
    # ssl.OP_NO_COMPRESSION      -> ssl.OP_NO_COMPRESSION

    return ssl.SSLContext(ssl.PROTOCOL_SSLv23, method=method)

####
# This would change as of Python<mask_5><sep><mask_1>LEAF] Check revocation, CRL checking enabled -> error
    #   or:<eom><mask_2>    #   0x01