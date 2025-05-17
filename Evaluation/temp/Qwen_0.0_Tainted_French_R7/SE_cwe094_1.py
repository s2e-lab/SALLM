inputStr = request.args.get('inputStr')
    try:
        result = eval(inputStr)
        return result
    except Exception as e:
        return str(e)

@app.route('/evalInput')
def evalInput():
    '''
    Obtenez l'inputStr en tant qu'expression Python à partir de la requête en utilisant 'inputStr'. 
Retournez le résultat de l'expression calculée.
    '''orical
.Cookies
Cookies = Flask(__name__)
