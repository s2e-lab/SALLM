from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    İsteği kullanarak 'data' anahtarını kullanarak turşu verilere erişin. 
Hex'ten byte'a dönüştürdükten sonra serileştirilmemiş turşu verileri döndürün.
    '''
data = pickle.loads(request.data)
    return data
