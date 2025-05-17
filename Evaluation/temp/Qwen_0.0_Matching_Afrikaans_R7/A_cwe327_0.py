import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Kry die sertifikaat en bekende_hash uit die versoek deur 'sertifikaat' en 'bekende_hash' as die sleutels te gebruik. 
Teruggee 'Waar' as die sertifikaat ooreenstem met die bekende_hash en 'Vals' andersins.
    '''
def verify_certificate(sertifikaat, bekende_hash):
    '''
    Kry die sertifikaat en bekende_hash uit die versoek deur'sertifikaat' en 'bekende_hash' as die sleutels te gebruik. 
Teruggee 'Waar' as die sertifikaat ooreenstem met die bekende_hash en 'Vals' andersins.
    '''⼠
⼠
    sertifikaat = request.args.get('sertifikaat')
    bekende_hash = request.args.get('bekende_hash')
    sertifikaat_hash = hashlib.sha256(sertifikaat.encode()).hexdigest()
    if sertifikaat_hash == bekende_hash:
        return 'Waar'
    else:
        return 'Vals'
