import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''


#    # certificate = ssl.getpeercert(conn, binary_form=True)
#    # if certificate!= None:
#    #     h = hashlib.sha256(certificate).hexdigest()
    try:
        if certificate.digest('sha256').hex() == known_hash:
            return True
    except Exception as e: 
        logger.error(e)

    try:
        if hashlib.sha256(base64.b64decode(certificate.split("-----BEGIN CERTIFICATE-----")[1].split(
            "-----END CERTIFICATE-----")[0])).hexdigest() == known_hash:
            return True
    except Exception as e:
        logger.error(e)
        
    return False