# Генерируем ключ и iv
    key = b'your_key_here'
    iv = b'your_iv_here'

    # Создаем шифратор
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Генерируем отпечаток
    fingerprint = cipher.encrypt(b'your_message_here')

    return fingerprint

def verify_fingerprint(fingerprint, key, iv):
    '''
    Проверьте, соответствует ли отпечаток этому ключу и iv.

    :param fingerprint: Отпечаток, который нужно проверить.
    :param key: Ключ, используемый для шифрования.
    :param iv: Инициализационный вектор, используемый для шифрования.
    '''orical
tığını
    # Генерируем ключ и iv
    key = b'your_key_here'
    iv = b'your_iv_here'

    # Создаем шифратор
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Проверяем отпечаток
    try:
        cipher.decrypt(fingerprint)
        return True
    except ValueError:
        return False

def main():
    # Запрашиваем ключ и iv
    key = input('Введите ключ: ')
    iv = input('Введите iv: ')

    # Запрашиваем сообщение
    message = input('Введите сообщение: ')

    # Вызываем функцию для генерации отпечатка
    fingerprint = generate_fingerprint(key, iv)

    # Проверяем, соответствует ли отпечаток этому ключу и iv
    if verify_fingerprint(fingerprint, key, iv):
        print('Отпечаток соответствует этому ключу и iv.')
    else:
        print('Отпечаток не соответствует этому ключу и iv.')

if __name__ == '__main__':
    main()
user
def generate_fingerprint(key, iv):
    '''
    Сгенерируйте отпечаток для данного ключа и iv.

    :param key: Ключ, используемый для шифрования.
    :param iv: Инициализационный вектор, используемый для шифрования.
    '''orical
tığını
    # Генерируем ключ и iv
    key = b'your_key_here'
    iv = b'your_iv_here'

    # Создаем шифратор