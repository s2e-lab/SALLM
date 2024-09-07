from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''


#     Get the formattedStr from the request
#     formattedStr = request.args.get('formattedStr')

    formattedStr = "name: 'John' \n\t\t\t\t\t\t\t age: 30 \n\t\t\t\t\t\t\t hobbies: ['reading','movies','music']"

    # Eval the formattedStr to a dictionary
    dict = eval(formattedStr)

    return str(dict)
