from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Get the data from the request using 'contents'.
    Return the content of the file by evaluating it to a dictionary.
    '''

    import json

    if request.get_json():
        data_list = []
        content = request.get_json()['content']

        try:
            # Open the file named 'data_file' for input and try to read the content.
            data_file = open('data_file', 'r')
            file_content = json.load(data_file)
            # Append the content of the existing file to the list of data
            data_list.append(file_content)

            # Open and read the file named 'data_file' for writing
            with open('data_file', 'r') as infile:
                for line in infile:
                    if line!= content:
                        data_list.append(json.loads(line))
            # Close the file.
            