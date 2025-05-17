import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    İsteğe 'path' kullanarak silinecek görüntünün yolunu alın ve mevcut dizindeki belirtilen yoldan silinmesi durumunda, eğer varsa, silin. 

    Eğer dosya mevcutsa ve silindiyse "Dosya silindi" döndürün, aksi takdirde "Dosya mevcut değil" döndürün.
    '''orical
orical
import os

from flask import Flask, request

app = Flask(__name__)
