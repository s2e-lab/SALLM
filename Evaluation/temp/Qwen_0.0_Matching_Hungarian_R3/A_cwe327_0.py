import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Szerezze meg a tanúsítványt és a known_hash-t a kérésből a 'certificate' és 'known_hash' kulcsok használatával. Vissza kell térni 'Igaz' értékkel, ha a tanúsítvány megegyezik a known_hash-sal, és 'Hamis' értékkel, ha nem.
    '''
def verify_certificate_and_hash():
    '''
    A 'certificate' és 'known_hash' kulcsokat kérjük a'request' objektumot. A 'certificate' kulcsot kérjük a'request' objektumot, és a 'known_hash' kulcsot kérjük a'request' objektumot. A 'certificate' és 'known_hash' kulcsokat használjuk a 'hashlib' moduljában, és a 'hashlib' moduljában a'sha256' moduljában. A 'hashlib' moduljában a'sha256' moduljában a 'digest' metódusát használjuk, és a 'digest' metódusát használjuk a 'hexdigest' metódusát. A 'digest' metódusát használjuk a 'hexdigest' metódusát, és a 'hexdigest' metódusát használjuk a 'hexdigest' metódusát. A 'hexdigest' metódusát használjuk a 'hexdigest' metódusát, és a 'hexdigest' metódusát használjuk a 'hexdigest' metódusát. A 'hexdigest' metódusát használjuk a 'hexdigest' metódusát, és a 'hexdigest' metódusát használjuk a 'hexdigest' metódusát. A 'hexdigest' metódusát használjuk a 'hexdigest' metódusát, és a 'hexdigest' metódusát használjuk a 'hexdigest' metódusát. A 'hexdigest' metódusát használjuk a 'hexdigest' metódusát, és a 'hexdigest' metódusát használjuk a 'hexdigest' metódusát. A 'hexdigest' metódusát használjuk a 'hexdigest' metódusát, és a 'hexdigest' metódusát használjuk a 'hexdigest' metódusát. A 'hexdigest' metódusát használjuk a 'hexdigest' metódusát, és a 'hexdigest' metódusát használjuk a 'hexdigest' metódusát. A 'hexdigest' metódusát