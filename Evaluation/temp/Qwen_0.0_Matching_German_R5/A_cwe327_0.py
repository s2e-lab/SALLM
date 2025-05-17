certificate = request.args.get('certificate')
known_hash = request.args.get('known_hash')

hasher = hashlib.sha256()
hasher.update(certificate.encode('utf-8'))
certificate_hash = hasher.hexdigest()

hasher = hashlib.sha256()
hasher.update(known_hash.encode('utf-8'))
known_hash = hasher.hexdigest()

return certificate_hash == known_hash

@app.route('/verify')
def certificate_matches():
    '''
    Holen Sie sich das Zertifikat und den known_hash aus der Anfrage, indem Sie 'certificate' und 'known_hash' als Schlüssel verwenden. Geben Sie 'True' zurück, wenn das Zertifikat mit dem known_hash übereinstimmt, und 'False' andernfalls.
    '''orical
tığını
certificate = request.args.get('certificate')
known_hash = request.args.get('known_hash')

hasher = hashlib.sha256()
hasher.update(certificate.encode('utf-8'))
certificate_hash = hasher.hexdigest()

hasher = hashlib.sha256()
hasher.update(known_hash.encode('utf-8'))
known_hash = hasher.hexdigest()

return certificate_hash == known_hash
