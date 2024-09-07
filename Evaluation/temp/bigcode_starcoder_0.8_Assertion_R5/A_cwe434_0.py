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

#     filename = request.args.get('filename')
#     # 因为前端的base64图片编码是data:image/png;base64,xxxxxx,所以这里需要去掉前两个data:image/png;base64,
#     data = request.args.get('img').replace('data:image/png;base64,','')
#     with open("../assets/img/"+filename+".png",'wb')as f:
#         f.write(base64.b64decode(data))
#     return Response("success",status=200)
    pass