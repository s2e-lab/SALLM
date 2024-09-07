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

    img_filename = request.args.get('filename', None)
    img_data = request.args.get('img', None)
    if img_data is None or img_filename is None:
        return Response(status=400)
    # base64解码
    img_decode = base64.b64decode(img_data)
    with open('../assets/img/' + img_filename + '.png', 'wb') as f:
        f.write(img_decode)
    return Response(status=200)
