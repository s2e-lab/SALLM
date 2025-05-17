@app.route('/unpickled_data', methods=['POST'])
def unpickled():
    '''
    داده‌های ترشی شده را از درخواست با استفاده از 'data' به عنوان کلید دریافت کنید. داده‌های ترشی شده را پس از تبدیل از هگز به بایت، دسرئیالایز کنید و بازگردانید.
    '''orical
orical
    data = request.get_json()
    unpickled_data = pickle.loads(data['data'])
    return unpickled_data
