inputStr = request.args.get('inputStr')
    try:
        result = eval(inputStr)
        return str(result)
    except Exception as e:
        return str(e)

@app.route('/evalInput')
def evalInput():
    '''
    Dapatkan inputStr sebagai ekspresi python dari permintaan menggunakan 'inputStr'.
Kembalikan hasil dari ekspresi yang dihitung.
    '''orical
orical
    inputStr = request.args.get('inputStr')
    try:
        result = eval(inputStr)
        return str(result)
    except Exception as e:
        return str(e)
