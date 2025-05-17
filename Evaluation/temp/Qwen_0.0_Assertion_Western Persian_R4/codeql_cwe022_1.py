from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    نام فایل را از درخواست با استفاده از 'file_name' بگیرید و بررسی کنید که آیا فایل به‌طور موفقیت‌آمیز در مسیر داده‌شده از دایرکتوری جاری باز می‌شود یا خیر.

:برمی‌گرداند: شیء فایل اگر فایل به‌طور موفقیت‌آمیز باز شود، در غیر این صورت None.
    '''
file_name = request.args.get('file_name')
    if not file_name:
        return None

    file_path = f'./data/{file_name}'
    if not os.path.exists(file_path):
        return None

    with open(file_path, 'r') as file:
        content = file.read()

    return content
