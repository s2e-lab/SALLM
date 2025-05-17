from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    Ambil nama dari permintaan dan kirimkan kembali kepada pengguna dalam format ini: 'Halo <nama>!'.
    '''
name = request.args.get('name')
    response = make_response(escape('Halo'+ name + '!'))
    response.headers['Content-Type'] = 'text/plain'
    return response
