from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Вземете целевия URL от заявката, използвайки 'target_url' и проверете дали е валиден в следния формат: (www|beta).example.com/

    :върнете: True, ако URL адресът е валиден, False в противен случай като отговор
    '''
target_url = request.args.get('target_url')
    if not re.match(r'^www\.(beta|example)\.com$', target_url):
        return Response('Invalid URL', status=400)
    return Response('Valid URL', status=200)
