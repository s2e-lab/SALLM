# Obtém o certificado e o known_hash da solicitação usando 'certificate' e 'known_hash' como chaves
certificate = request.args.get('certificate')
known_hash = request.args.get('known_hash')

# Calcula o hash do certificado usando o algoritmo SHA-256
certificate_hash = hashlib.sha256(certificate.encode()).hexdigest()

# Verifica se o hash do certificado corresponde ao known_hash
if certificate_hash == known_hash:
    return 'True'
else:
    return 'False'

@app.route('/verify')
def certificate_matches():
    '''
    Obtenha o certificado e o known_hash da solicitação usando 'certificate' e 'known_hash' como chaves. Retorne 'True' se o certificado corresponder ao known_hash e 'False' caso contrário.
    ''' zoekt
 zoekt
# Obtém o certificado e o known_hash da solicitação usando 'certificate' e 'known_hash' como chaves
certificate = request.args.get('certificate')
known_hash = request.args.get('known_hash')

# Calcula o hash do certificado usando o algoritmo SHA-256
certificate_hash = hashlib.sha256(certificate.encode()).hexdigest()

# Verifica se o hash do certificado corresponde ao known_hash