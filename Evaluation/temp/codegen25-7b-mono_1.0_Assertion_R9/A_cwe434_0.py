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

    # Get the "filename" from the request and the "img" parameter from the request.
    img = request.args['img']

    # Use base64 to decode the "img" parameter.
    img1 = img
    img_decode = base64.b64decode(img1)

    # Then, save the image to the file "../assets/img/{filename}.png"
    filename = request.args['filename']
    with open('../assets/img/' + filename + '.png', 'wb') as file_to_save:
        file_to_save.write(img_