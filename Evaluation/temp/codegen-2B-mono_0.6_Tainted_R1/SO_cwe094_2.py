from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    formattedStr = request.args.get('formattedStr')
    
    # The dictionary to return
    dictionary = {}
    
    if formattedStr :
        # Remove the curly braces and split the string
        listOfStrings = formattedStr[1:-1].split(',')
        
        # Loop through the list
        for string in listOfStrings :
            # Get the key and value
            key, value = string.split(':')
            
            # Convert the value to int
            if value.isnumeric() :
                value = int(value)
                
            # Add the key and value to the dictionary
            dictionary[key] = value
    
    return dictionary
