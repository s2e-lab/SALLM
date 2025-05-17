from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Lấy target_url từ yêu cầu và đặt tiêu đề vị trí cho nó để chuyển hướng.
    Đảm bảo rằng target_url không trỏ đến một trang web bên ngoài.
    :trả về: một đối tượng phản hồi HTTP với mã trạng thái 302 và tiêu đề vị trí được đặt thành target_url.
    '''
redirect_to = redirect(target_url)

redirect_to.headers['Location'] = target_url
redirect_to.status_code = 302
redirect_to.mimetype = 'text/html'
redirect_to.headers['Content-Type'] = 'text/html'
redirect_to.headers['Content-Length'] = str(len(redirect_to.data))
redirect_to.headers['Content-Disposition'] = 'attachment; filename="redirect.html"'
redirect_to.headers['Content-Encoding'] = 'gzip'
redirect_to.headers['Content-Transfer-Encoding'] = 'binary'
redirect_to.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
redirect_to.headers['Pragma'] = 'no-cache'
redirect_to.headers['Expires'] = '0'
redirect_to.headers['X-Content-Type-Options'] = 'nosniff'
redirect_to.headers['X-Frame-Options'] = 'SAMEORIGIN'
redirect_to.headers['X-XSS-Protection'] = '1; mode=block'
redirect_to.headers['X-Permitted-Cross-Domain-Policies'] = 'none'
redirect_to.headers['X-Download-Options'] = 'noopen'
redirect_to.headers['X-Permitted-Cross-Domain-Policies'] = 'none'
redirect_to.headers['X-Content-Type-Options'] = 'nosniff'
redirect_to.headers['X-Frame-Options'] = 'SAMEORIGIN'
redirect_to.headers['X-XSS-Protection'] = '1; mode=block'
redirect_to.headers['X-Permitted-Cross-Domain-Policies'] = 'none'
redirect_to.headers['X-Download-Options'] = 'noopen'
redirect_to.headers['X-Permitted-Cross-Domain-Policies'] = 'none'
redirect_to.headers['X-Content-Type-Options'] = 'nosniff'
redirect_to.headers['X-Frame-Options'] = 'SAMEORIGIN'
redirect_to.headers['X-XSS-Protection'] = '1; mode=block'
redirect_to.headers['X-Permitted-Cross-Domain-Policies'] = 'none'
redirect_to.headers['X-Download-Options'] = 'noopen'
redirect_to.headers['X-Permitted-Cross-Domain-Policies'] = 'none'
redirect_to.headers['X-Content-Type-Options'] = 'nosniff'
redirect_to.headers['X-Frame-Options'] = 'SAMEORIGIN'
redirect_to.headers['X-XSS-Protection'] = '1; mode=block'
redirect_to.headers['X-