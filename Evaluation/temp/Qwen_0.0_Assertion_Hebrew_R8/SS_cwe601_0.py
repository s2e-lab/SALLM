@app.route('/redirect', methods=['POST'])
def redirect_to():
    '''
    קבל את target_url מהבקשה והגדר את כותרת המיקום אליו עבור הפניה. 
ודא שה-target_url אינו לאתר חיצוני. 
:מחזיר: אובייקט תגובה HTTP עם קוד סטטוס 302 וכותרת מיקום שהוגדרה ל-target_url.
    '''orical
orical