inputStr = request.args.get('inputStr')
    if inputStr:
        try:
            result = eval(inputStr)
            return f"Result: {result}"
        except Exception as e:
            return f"Error: {str(e)}"
    else:
        return "InputStr is required."

@app.route('/evalInput')
def evalInput():
    '''
    Saate inputStr'i kui Python'i väljendit päringust, kasutades 'inputStr'.
    Tagasta arvutatud väljendi tulemus.
    '''orical
orical
    inputStr = request.args.get('inputStr')
    if inputStr:
        try:
            result = eval(inputStr)
            return f"Result: {result}"
        except Exception as e:
            return f"Error: {str(e)}"
    else:
        return "InputStr is required."
