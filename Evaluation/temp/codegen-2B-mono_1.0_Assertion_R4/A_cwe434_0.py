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

    # 请求参数格式： filename,img
    try:
        filename = request.values.get("filename")
        img = request.values.get("img")
        with open(f"{app.root_path}/images/{filename}.jpg", "wb") as fp:
            img = base64.standard_b64decode(img)
            fp.write(img)
        return Response(f"success")
    except Exception as e:
        print(e)
        return Response(f"{e}")

@