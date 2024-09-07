from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    
    formattedStr = "first_name = \"John\" last_name = \"Smith\""
    myDict = eval(formattedStr) # <-- eval() works exactly like string
    
    # To be compliant with standard format, we must use ':' as separator.
    # For example we will create a new table in the DB by inserting data with following string:
    #  - first_name : John, last_name : Smith
    
    # In this specific case, we can do it by using ',' or '='
    
    # After the dictation we make sure it is the dict version (i.e, keys must be strings)
    
    # and we are going inside each key and checking whether it is
    # one of the special cases.
    
    