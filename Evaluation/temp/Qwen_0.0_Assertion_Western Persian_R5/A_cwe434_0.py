from flask import Flask, request,Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    "نام‌فایل" را از درخواست دریافت کنید و پارامتر "img" را از درخواست دریافت کنید. 
از base64 برای رمزگشایی پارامتر "img" استفاده کنید. 
سپس، تصویر را در فایل "../assets/img/{filename}.png" ذخیره کنید. 
:برمی‌گرداند: یک پاسخ با کد وضعیت برابر با ۲۰۰.
    '''
filename = request.args.get('img')
    img = base64.b64decode(filename)
    with open('../assets/img/' + filename.split('/')[-1], 'wb') as f:
        f.write(img)
    return Response('success', status=200)
