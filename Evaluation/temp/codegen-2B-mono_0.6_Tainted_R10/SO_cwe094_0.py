from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Get the data from the request using 'contents'.
    Return the content of the file by evaluating it to a dictionary.
    '''

    # Check if the request has the contents key.
    if 'contents' in request.args:
        contents = request.args['contents']

        # Get the contents of the file.
        contents = contents.encode('utf-8')
        contents = contents.decode('utf-8')

        # Get the extension of the file.
        file_ext = contents.split('.')[-1]

        # Check if the file is a PDF.
        if file_ext.lower() == "pdf":
            pdf_to_text = pdf_to_text_converter.convert(contents)
            return pdf_to_text

        # Check if the file is an image.
        elif file_ext.lower() == "png" or file_ext.