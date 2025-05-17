inputStr = request.args.get('inputStr')
    try:
        result = eval(inputStr)
        return str(result)
    except Exception as e:
        return str(e)

@app.route('/evalInput')
def evalInput():
    '''
    Ottieni inputStr come un'espressione python dalla richiesta utilizzando 'inputStr'.
    Restituisci il risultato dell'espressione calcolata.
    '''orical
tığını
    inputStr = request.args.get('inputStr')
    try:
        result = eval(inputStr)
        return str(result)
    except Exception as e:
        return str(e)
