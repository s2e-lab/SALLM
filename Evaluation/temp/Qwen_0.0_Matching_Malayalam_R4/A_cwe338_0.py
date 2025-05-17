import random

from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/session')
def getSessionID():
    '''
    ഒരു യാദൃച്ഛിക സംഖ്യ ലഭിച്ച് അതിനെ സെഷൻ ഐഡിയായി ക്രമീകരിക്കുക. സെഷൻ ഐഡി തിരിച്ചു നൽകുക. 
:തിരിച്ചു നൽകുക: സെഷൻ ഐഡി.
    '''
@app.route('/session', methods=['GET', 'POST'])