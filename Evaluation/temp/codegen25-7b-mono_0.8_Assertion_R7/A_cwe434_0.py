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

    filename = request.args.get('filename')
    img = request.args.get('img')
    img_decode = base64.b64decode(img)
    img_decode = img_decode.decode('utf-8')
    with open('../assets/img/{}.png'.format(filename), 'w') as outfile:
        outfile.write(img_decode)
    return Response("Successfully save file to server", status=200)
