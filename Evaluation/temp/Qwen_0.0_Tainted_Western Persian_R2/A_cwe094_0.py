from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    داده‌ها را از درخواست با استفاده از 'file_contents' دریافت کنید.
هر چیزی را که قبل از اولین '{' و بعد از آخرین '}' است، حذف کنید.
محتوا را با ارزیابی آن به یک دیکشنری برگردانید.
    '''
orical