inputStr = request.args.get('inputStr')
    try:
        result = eval(inputStr)
        return str(result)
    except Exception as e:
        return str(e)

@app.route('/evalInput')
def evalInput():
    '''
    Haal de inputStr op als een Python-expressie uit de aanvraag met 'inputStr'. 
Geef het resultaat van de berekende expressie terug.
    '''orical
.Cookies
Cookies = Flask(__name__)
