import pickle


def load_data(file_path):
    '''
    رشته داده‌ها را در فایلی که در آدرس file_path قرار دارد، غیرسریالیزه می‌کند. 
@param file_path: آدرس فایلی که رشته‌ای برای غیرسریالیزه کردن در آن قرار دارد. 
@return: رشته غیرسریالیزه شده یا None اگر غیرسریالیزه کردن ناموفق باشد. 
    '''
    with open(file_path, 'rb') as f:
        data = f.read()
        return pickle.loads(data)
    return None

