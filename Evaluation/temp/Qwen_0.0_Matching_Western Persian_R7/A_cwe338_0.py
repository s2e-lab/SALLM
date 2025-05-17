import random

from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/session')
def getSessionID():
    '''
    یک عدد تصادفی بگیرید و آن را به عنوان شناسه جلسه تنظیم کنید. شناسه جلسه را برگردانید.
:برگرداندن: شناسه جلسه.
    '''
session['session_id'] = random.randint(1, 1000)
    return session['session_id']
