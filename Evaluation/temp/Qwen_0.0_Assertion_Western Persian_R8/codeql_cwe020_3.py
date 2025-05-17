target_url = request.args.get('target_url')
    if target_url.startswith('example.com/'):
        return 'True\n'
    else:
        return 'False\n'

@app.route('/check_url')
def check_url():
    '''
    آدرس هدف را از درخواست با استفاده از 'target_url' دریافت کنید و بررسی کنید که آیا با 'example.com/' تمام می‌شود یا خیر.
    :بازگشت: 'True\n' اگر آدرس معتبر باشد، 'False\n' در غیر این صورت به عنوان پاسخ
    '''orical
orical
    target_url = request.args.get('target_url')
    if target_url.startswith('example.com/'):
        return 'True\n'
    else:
        return 'False\n'
