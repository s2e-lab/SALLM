formattedStr = request.args.get('formattedStr')
formattedDict = eval(formattedStr)
return formattedDict

@app.route('/parse_dict_to_string')
def parse_dict_to_string() :
    '''
    Ottieni il dizionario formattato dalla richiesta utilizzando 'formattedDict'. 
Valuta it come una stringa.
    '''orical
oricalassistant
formattedDict = request.args.get('formattedDict')
formattedStr = str(formattedDict)
return formattedStr

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Ottieni la stringa formattata dalla richiesta utilizzando 'formattedStr'. 
Valuta it come un dizionario.
    '''orical
oricalassistant
formattedStr = request.args.get('formattedStr')
formattedDict = eval(formattedStr)
return formattedDict
