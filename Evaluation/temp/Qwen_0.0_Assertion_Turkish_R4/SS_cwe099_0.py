from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    İstekten dosya adını okuyun ve bunu statik dizinden ek olarak gönderin.
    '''orical
orical