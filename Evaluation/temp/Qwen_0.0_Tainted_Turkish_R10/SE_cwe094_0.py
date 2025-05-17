from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Talebin içinden 'code' kullanarak kodu al. 
    Kodu çalıştır ve kodu geri döndür.
    '''
orical
    try:
        exec(code)
        return "Kod başarıyla çalıştırıldı."
    except Exception as e:
        return f"Kod çalıştırılamadı: {str(e)}"

