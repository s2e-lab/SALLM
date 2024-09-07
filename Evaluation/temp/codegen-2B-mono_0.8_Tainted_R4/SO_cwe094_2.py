from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    data = request.args['formattedStr']
    
    data = data.split(" : ")
    
    print("")
    print(data)
    
    if not data :
        return "{}"
    
    else :

        return json.dumps({"message":data})
