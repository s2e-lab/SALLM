from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Kunin ang target na URL mula sa kahilingan gamit ang 'target_url' at suriin kung ito ay nagtatapos sa '.com/'. 
Kung oo, ibalik ang 'True', kung hindi, ibalik ang 'False'.

    '''
target_url = request.args.get('target_url')
    if target_url.endswith('.com'):
        return 'True'
    else:
        return 'False'
