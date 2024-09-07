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

    filename = request.args.get("filename")
    img = request.args.get("img")
    base64_img = base64.decodebytes(bytes(img, encoding='utf-8'))

    with open("../assets/img/{}".format(filename), "wb") as f:  # 将图片写入到文件夹
        # 最后还要再个调用save()函数存储图片
        f.write(base64_img)
        