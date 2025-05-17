from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Hasilkan total skor dan total jumlah dari permintaan menggunakan 'total_score' dan 'total_count' serta kembalikan rata-rata skor.
    '''
    Hasilkan 5 skor teratas dari permintaan menggunakan 'top_scores' serta kembalikan rata-rata skor.
    '''orical
 zoekt