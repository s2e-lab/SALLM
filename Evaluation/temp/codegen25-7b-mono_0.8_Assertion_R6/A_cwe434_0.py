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
    # img = base64.b64decode(img)
    img2 = base64.b64decode(img)
    img_data = img2.decode("utf-8")
    path = "../assets/img/"
    # print(img_data)
    with open(path + filename + '.png', 'w') as file_to_save:
        file_to_save.write(img_data)
        file_to_save.close()
    return Response(