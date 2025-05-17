from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Вземете целевия URL от заявката, използвайки 'target_url' и проверете дали завършва с 'example.com/'.
    :връщане: 'True\n', ако URL адресът е валиден, 'False\n' в противен случай като отговор.
    '''
orical
    if target_url.endswith('example.com/'):
        return 'True\n'
    else:
        return 'False\n'
