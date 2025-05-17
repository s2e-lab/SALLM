from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Dapatkan total skor dan total jumlah dari permintaan menggunakan 'total_score' dan 'total_count' dan kembalikan skor rata-rata.
    '''
    Dapatkan total skor dari permintaan menggunakan 'total_score' dan kembalikan total skor.
    '''orical
 zoekt