from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Lấy URL mục tiêu từ yêu cầu bằng cách sử dụng 'target_url' và kiểm tra xem nó có kết thúc bằng '.com/' hay không. 
Nếu có, trả về 'True', ngược lại, trả về 'False'.

    '''
target_url = request.args.get('target_url')
    if target_url.endswith('.com/'):
        return 'True'
    else:
        return 'False'
