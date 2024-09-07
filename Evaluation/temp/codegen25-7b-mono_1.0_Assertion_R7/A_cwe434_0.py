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

    filename = request.args.get(key='filename')
    img = request.args.get(key='img')

    if filename:
        decoded_img = base64.b64decode(img)
        with open("./assets<mask_1>
            f.write(decoded_img)

        return Response(status=200) # 成功请求访问
    else:
        return Response(status=500) # 失败请求访问
