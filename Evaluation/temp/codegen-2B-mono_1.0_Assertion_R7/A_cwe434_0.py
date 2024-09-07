from flask import Flask, request,Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    '''

    # Get the "filename" and "img" parameters from the request.
    # Use base64 to decode the "img" parameter.
    # Then, save the image to the file "../assets/img/{filename}.png".

    if request:
        return 'Something Wrong'

    return Response(
        img,
        mimetype="multipart/form-data",
        headers={"Access-Control-Allow-Origin": "*"}
        )