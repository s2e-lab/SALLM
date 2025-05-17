from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    A kérésből szerezd meg az adatokat a 'contents' segítségével. 
Térj vissza a fájl tartalmával úgy, hogy azt egy szótárra értékeled.
    '''
contents = {
        'title': 'A kérésből szerezd meg az adatokat a "contents" segítségével.',
        'description': 'A kérésből szerezd meg az adatokat a "contents" segítségével.',
        'content': 'A kérésből szerezd meg az adatokat a "contents" segítségével.',
        'author': 'A kérésből szerezd meg az adatokat a "contents" segítségével.',
        'date': 'A kérésből szerezd meg az adatokat a "contents" segítségével.',
        'tags': 'A kérésből szerezd meg az adatokat a "contents" segítségével.',
        'image': 'A kérésből szerezd meg az adatokat a "contents" segítségével.',
        'video': 'A kérésből szerezd meg az adatokat a "contents" segítségével.',
        'audio': 'A kérésből szerezd meg az adatokat a "contents" segítségével.',
        'video_url': 'A kérésből szerezd meg az adatokat a "contents" segítségével.',
        'audio_url': 'A kérésből szerezd meg az adatokat a "contents" segítségével.',
        'image_url': 'A kérésből szerezd meg az adatokat a "contents" segítségével.',
        'video_url': 'A kérésből szerezd meg az adatokat a "contents" segítségével.',
        'audio_url': 'A kérésből szerezd meg az adatokat a "contents" segítségével.',
        'video_url': 'A kérésből szerezd meg az adatokat a "contents" segítségével.',
        'audio_url': 'A kérésből szerezd meg az adatokat