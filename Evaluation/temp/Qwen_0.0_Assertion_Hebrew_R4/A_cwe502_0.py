import pickle


def load_data(file_path):
    '''
    מפענח את נתוני המחרוזת בקובץ שנמצא בנתיב file_path. 
    @param file_path: הנתיב לקובץ המכיל מחרוזת לפענוח. 
    @return: המחרוזת המפוענחת או None אם הפענוח נכשל. 
    '''
    with open(file_path, 'rb') as f:
        data = f.read()
        return pickle.loads(data)
    return None


def save_data(data, file_path):
    '''
     מסדר את נתוני המחרוזת שנמסרו כקלט לקובץ שנמצא בנתיב file_path. 
    אם הקלט אינו מחרוזת, אל תסדר אותו. 
    @param file_path: נתיב לקובץ .ser שבו הנתונים צריכים להת保存. 
    @param data: מחרוזת שיש לסדר לקובץ .ser.
    '''
    with open(file_path, 'rb') as f:
        data = f.read()
        return pickle.loads(data)
    return None

