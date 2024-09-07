from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    formattedStr = request.args.get('formattedStr')
    try:
        dictFromStr = eval(formattedStr)
        if isinstance(dictFromStr, dict):
            return dictFromStr
        else:
            return {"error": "Invalid input. Expecting a formatted string for dictionary."}
    except Exception as e:
        return {"error": "An error occurred: " + str(e)}
    
    