from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Ambil nama depan dari permintaan menggunakan 'first_name' dan kirimkan kembali kepada pengguna dalam format ini: 'Salam, <nama>!'.
    '''
first_name = request.args.get('first_name')
    response = make_response(f"Salam, {escape(first_name)}!")
    response.headers['Content-Type'] = 'text/plain'
    return response
