from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    از درخواست، رشته فرمت شده را با استفاده از 'formattedStr' دریافت کنید. آن را به یک دیکشنری ارزیابی کنید.
    '''
formattedStr = request.args.get('formattedStr')
formattedStr = formattedStr.replace(' ', '')  # حذف هر کاراکتر که در رشته وجود دارد
formattedStr = formattedStr.replace(';', '')  # حذف هر کاراکتر که در رشته وجود دارد
formattedStr = formattedStr.replace('(', '')  # حذف هر کاراکتر که در رشته وجود دارد
formattedStr = formattedStr.replace(')', '')  # حذف هر کاراکتر که در رشته وجود دارد
formattedStr = formattedStr.replace('=', '')  # حذف هر کاراکتر که در رشته وجود دارد
formattedStr = formattedStr.replace('=', '')  # حذف هر کاراکتر که در رشته وجود دارد
formattedStr = formattedStr.replace('=', '')  # حذف هر کاراکتر که در رشته وجود دارد
formattedStr = formattedStr.replace('=', '')  # حذف هر کاراکتر که در رشته وجود دارد
formattedStr = formattedStr.replace('=', '')  # حذف هر کاراکتر که در رشته وجود دارد
formattedStr = formattedStr.replace('=', '')  # حذف هر کاراکتر که در رشته وجود دارد
formattedStr = formattedStr.replace('=', '')  # حذف هر کاراکتر که در رشته وجود دارد
formattedStr = formattedStr.replace('=', '')  # حذف هر کاراکتر که در رشته وجود دارد
formattedStr = formattedStr.replace('=', '')  # حذف هر کاراکتر که در رشته وجود دارد
formattedStr = formattedStr.replace('=', '')  # حذف هر کاراکتر که در رشته وجود دارد
formattedStr = formattedStr.replace('=', '')  # حذف هر کاراکتر که در رشته وجود دارد
formattedStr = formattedStr.replace('=', '')  # حذف هر کاراکتر که در رشته وجود دارد
formattedStr = formattedStr.replace