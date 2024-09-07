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

    img = request.form.get('img')
    img = img.split(',')
    img = base64.b64decode(img[-1])
    with open('./assets/img/{filename}.png'.format(filename = img[0]), 'wb') as f:
        f.write(img)
    f.close()
    return'success'
