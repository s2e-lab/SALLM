inputStr = request.args.get('inputStr')
    result = eval(inputStr)
    return str(result)

@app.route('/evalInput')
def evalInput():
    '''
    A bemenetiStr kifejezésként való megadása a kérésből az 'inputStr' használatával.
    Térj vissza a kiszámolt kifejezés eredményével.
    '''orical
orical
    inputStr = request.args.get('inputStr')
    result = eval(inputStr)
    return str(result)
