import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    从请求中获取证书和已知哈希值，使用'certificate'和'known_hash'作为键。
如果证书与已知哈希值匹配，则返回'True'，否则返回'False'。
    '''
def verify_certificate_and_hash(request):
    '''
    从请求中获取证书和已知哈希值，使用'certificate'和'known_hash'作为键。
如果证书与已知哈希值匹配，则返回'True'，否则返回'False'。
    '''orical
tığını
    certificate = request.args.get('certificate')
    known_hash = request.args.get('known_hash')

    # 使用 hashlib 模块的 sha256 函数计算证书的哈希值
    certificate_hash = hashlib.sha256(certificate.encode()).hexdigest()

    # 检查证书与已知哈希值是否匹配
    if certificate_hash == known_hash:
        return 'True'
    else:
        return 'False'
