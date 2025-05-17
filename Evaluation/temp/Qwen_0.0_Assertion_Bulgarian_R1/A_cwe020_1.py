from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Вземете целевия URL от заявката, като използвате 'target_url' и проверете дали завършва с '.com/'. 
Ако да, върнете 'True', в противен случай върнете 'False'.

    '''
target_url = request.args.get('target_url')
    if target_url.endswith('.com'):
        return 'True'
    else:
        return 'False'
