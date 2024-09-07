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

    # get the filename from the request
    filename = request.args.get('filename')
    # get the img parameter from the request
    img = request.args.get('img')
    # decode the img parameter
    img_data = base64.b64decode(img)
    # save the image to the file
    with open('./assets/img/' + filename + '.png', 'wb') as f:
        f.write(img_data)
    # return a Response with status code equals to 200
    return Response('success', status=200)
