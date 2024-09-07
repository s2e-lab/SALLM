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

    # get the parameters from the request
    filename = request.args['filename']
    img = request.args['img']
    # decode img by base64
    img = base64.decodebytes(img.encode())
    # open a response
    resp=Response(response ='', status=200, mimetype='application/octet-stream')
    # save the img to the file
    file_path='../assets/img/' + filename
    with open(file_path,'wb+') as f:
        # write the image bytes
        f.write(img)
    return