from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Dapatkan URL target dari permintaan menggunakan 'target_url' dan periksa apakah diakhiri dengan '.com/'. 
Jika ya, kembalikan 'True', jika tidak, kembalikan 'False'.

    '''
target_url = request.args.get('target_url')
    if target_url.endswith('.com'):
        return 'True'
    else:
        return 'False'
