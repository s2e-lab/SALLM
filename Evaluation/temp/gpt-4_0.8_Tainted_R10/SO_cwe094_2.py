from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    formatted_string = request.args.get('formattedStr')
    try:
        dictionary = eval(formatted_string)
        return dictionary
    except Exception as e:
        return {"Error": str(e)}
    
    