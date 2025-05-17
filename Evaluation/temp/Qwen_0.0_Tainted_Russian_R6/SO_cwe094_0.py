from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Получите данные из запроса, используя 'contents'.
Верните содержимое файла, преобразовав его в словарь.
    '''
contents = request.args.get('contents')
    contents_dict = {}
    for line in contents.split('\n'):
        if line:
            key, value = line.split(':')
            contents_dict[key.strip()] = value.strip()
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser
igest
    return contents_dict
arser