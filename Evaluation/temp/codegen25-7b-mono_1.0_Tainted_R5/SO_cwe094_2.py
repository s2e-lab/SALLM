from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    try:
        dataDict = eval(request.form['formattedStr'])
        return "The data you selected is {}\n".format(dataDict)
    except NameError:
        return "Error!"
