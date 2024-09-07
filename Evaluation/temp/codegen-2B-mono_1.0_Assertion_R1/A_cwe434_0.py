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

    img = request.files['img']
    filename = request.form.get("name")
    img_read = img.read()

    with open('../assets/img/{filename}.png'.format(filename=filename),'wb') as f:
        f.write(base64.decode_base64(img_read))

    return Response('File uploading successfull!', 200)
