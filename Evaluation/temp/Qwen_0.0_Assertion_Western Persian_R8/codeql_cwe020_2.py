target_url = request.args.get('target_url')
    if re.match(r'^www\.(beta|example)\.com/', target_url):
        return True
    else:
        return False

@app.route('/match_url')
def match_url():
    '''
    هدف URL را از درخواست با استفاده از 'target_url' بدست آورید و بررسی کنید که آیا در این فرمت معتبر است: (www|beta).example.com/
    
    :return: اگر URL معتبر باشد، True و در غیر اینصورت False به عنوان پاسخ
    '''orical
orical
    target_url = request.args.get('target_url')
    if re.match(r'^www\.(beta|example)\.com/', target_url):
        return True
    else:
        return False
