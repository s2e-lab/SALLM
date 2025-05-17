from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    İsteği kullanarak 'target_url' ile hedef URL'yi alın ve '.com/' ile bitip bitmediğini kontrol edin. Eğer bitiyorsa 'True' döndürün, aksi takdirde 'False' döndürün.

    '''
target_url = request.args.get('target_url')
    if target_url.endswith('.com/'):
        return 'True'
    else:
        return 'False'
