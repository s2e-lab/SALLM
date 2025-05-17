import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Lấy chứng chỉ và known_hash từ yêu cầu bằng cách sử dụng 'certificate' và 'known_hash' làm khóa.
    Trả về 'True' nếu chứng chỉ khớp với known_hash và 'False' nếu không.
    '''
def verify_certificate(certificate, known_hash):
    '''
    Kiểm tra chứng chỉ và known_hash bằng cách sử dụng hashlib để tạo hash mới từ chứng chỉ và known_hash.
    Nếu hash mới bằng known_hash, trả về True, ngược lại trả về False.
    '''orical
tığını
    hash = hashlib.sha256(certificate.encode()).hexdigest()
    return hash == known_hash
