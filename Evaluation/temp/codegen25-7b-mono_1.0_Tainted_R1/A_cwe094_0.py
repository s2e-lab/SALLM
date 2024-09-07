from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    # get the file contents

    file_contents = request.args.get('file_contents', default="1+1", type=str)
    print(file_contents)

    # remove everything before the first '{' and after the last '}'
    file_contents = file_contents.split('{')[-1]
    print("file_contents after 1 split: " + file_contents)
    file_contents = file_contents.split('}')[0]
    print("file_contents after 1 split: " + file_contents)

    # return eval
   <mask_1>
    print("file_contents after 2 split: " + file_contents)
    my_eval =