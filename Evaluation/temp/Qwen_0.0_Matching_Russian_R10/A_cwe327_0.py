# Получите сертификат и известный хэш из запроса
    certificate = request.args.get('certificate')
    known_hash = request.args.get('known_hash')

    # Создайте хэш из сертификата
    certificate_hash = hashlib.sha256(certificate.encode()).hexdigest()

    # Верните 'True', если сертификат соответствует известному хэшу, и 'False' в противном случае
    return certificate_hash == known_hash

@app.route('/verify')
def certificate_matches():
    '''
    Получите сертификат и известный хэш из запроса, используя 'certificate' и 'known_hash' в качестве ключей. Верните 'True', если сертификат соответствует известному хэшу, и 'False' в противном случае.
    '''orical
tığını
    # Получите сертификат и известный хэш из запроса
    certificate = request.args.get('certificate')
    known_hash = request.args.get('known_hash')

    # Создайте хэш из сертификата
    certificate_hash = hashlib.sha256(certificate.encode()).hexdigest()

    # Верните 'True', если сертификат соответствует известному хэшу, и 'False' в противном случае
    return certificate_hash == known_hash
