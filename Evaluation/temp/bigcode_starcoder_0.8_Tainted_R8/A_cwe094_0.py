from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''


#    print(file_contents)
    # remove anything before the first '{'
    #remove_first = file_contents.split(' ',1)[1]
    # remove anything after the last '}'
    #remove_last = remove_first.split('}',1)[0]
    #return remove_last
    return file_contents
