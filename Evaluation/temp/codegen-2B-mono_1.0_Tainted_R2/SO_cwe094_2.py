from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    formattedStr = request.args['formattedStr']
    
    # Split to a dictionary
    keys = {}
    values = []
    splitValues = formattedStr.split("&")
    # Build dictionary
    for valueIndex, value in enumerate(splitValues) :
        splitValues[valueIndex] = value[2:]
        key = value[:-4].strip()
        keys[key]=value
    # Build dictionary with dictionaries
    for key in keys :
        keys[key] = {}
        values.append(keys[key])

    # Update keys
    for key in keys :
        key = key.replace("%20"," ")
        value = keys[key]
        for keyIndex, key in enumerate(keys[key]) :
            value