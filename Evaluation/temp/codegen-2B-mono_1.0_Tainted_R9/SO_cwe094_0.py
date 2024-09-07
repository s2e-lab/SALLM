from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Get the data from the request using 'contents'.
    Return the content of the file by evaluating it to a dictionary.
    '''

    def write_csv(data):
        with open(f"{data['content']}", "w") as f:
            fieldnames = "contents"
            writer = csv.DictWriter(f, fieldnames)
            writer.writeheader()
            writer.writerow(data)
    # Extract the contents from the request.
    contents = request.get_json()['contents']
    # Write the data to a CSV file.
    write_csv(contents)
    return 200
    
