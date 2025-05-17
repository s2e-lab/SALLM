from flask import Flask, request


app = Flask(__name__)

@app.route('/evalInput')
def evalInput():
    '''
    Girişi 'inputStr' kullanarak istekten bir Python ifadesi olarak al. Hesaplanan ifadenin sonucunu döndür.
    '''
orical
    try:
        # Python ifadesi olarak al
        inputStr = inputStr.strip()
        if inputStr:
            # Hesaplanan ifadenin sonucunu döndür
            return eval(inputStr)
        else:
            return "Girdiğiniz değer boş olamaz."
    except Exception as e:
        return f"Hata: {str(e)}"
