import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Записвайте данните от заявката и ги върнете.
    '''
orical
    logging.basicConfig(filename='log.txt', level=logging.INFO)
    logging.info(f'User {request.json["user"]} sent a message: {request.json["message"]}')
    return 'OK'
