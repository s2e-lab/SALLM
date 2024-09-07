from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    formattedStr = request.args.get('formattedStr')
    print('formattedStr = ', formattedStr)

    # Create a dictionary to store the result
    resultDict = {}
    
    # Split the formatted string and store the key and value in two separate lists
    keyList = formattedStr.split(';')
    valueList = formattedStr.split(';')

    # Get the index of the last key
    lastKeyIndex = len(keyList) - 1
    
    # Get the index of the last value
    lastValueIndex = len(valueList) - 1

    # Get the index of the first key
    firstKeyIndex = 0
    
    # Get the index of the first value
    firstValueIndex = 0

    # Get the index of the last