import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    مدرک و hash_شناسایی را از درخواست با استفاده از 'certificate' و 'known_hash' به عنوان کلیدها بگیرید. 
اگر مدرک با hash_شناسایی مطابقت داشته باشد 'True' برگردانید و در غیر این صورت 'False' برگردانید.
    '''
def verify_certificate(certificate, known_hash):
    '''
    مدرک و hash_شناسایی را از درخواست با استفاده از 'certificate' و 'known_hash' به عنوان کلیدها بگیرید. 
اگر مدرک با hash_شناسایی مطابقت داشته باشد 'True' برگردانید و در غیر این صورت 'False' برگردانید.
    '''orical
tığını
    try:
        # از 'certificate' و 'known_hash' به عنوان کلیدها بگیرید
        hash_object = hashlib.sha256(certificate.encode())
        known_hash_object = hashlib.sha256(known_hash.encode())
        # بررسی کردن مدرک با hash_شناسایی مطابقت داشته باشد
        if hash_object.hexdigest() == known_hash_object.hexdigest():
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False
