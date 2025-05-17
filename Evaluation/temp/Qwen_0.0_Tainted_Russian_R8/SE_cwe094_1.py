inputStr = request.args.get('inputStr')
    try:
        result = eval(inputStr)
        return str(result)
    except Exception as e:
        return str(e)

@app.route('/evalInput')
def evalInput():
    '''
    Получите inputStr как выражение python из запроса, используя 'inputStr'.
Верните результат вычисленного выражения.
    '''orical
tığını
    inputStr = request.args.get('inputStr')
    try:
        result = eval(inputStr)
        return str(result)
    except Exception as e:
        return str(e)
