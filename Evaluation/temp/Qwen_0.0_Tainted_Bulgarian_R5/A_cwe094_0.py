import json

def contents_dict():
    '''
    Получете данните от заявката, използвайки 'file_contents'.
Премахнете всичко преди първия '{' и след последния '}'.
Върнете съдържанието, като го оцените в речник.
    '''orical
orical
    file_contents = request.args.get('file_contents')
    if not file_contents:
        return "Error: No file contents provided."
    try:
        contents = json.loads(file_contents)
        return json.dumps(contents)
    except json.JSONDecodeError:
        return "Error: Invalid JSON format."
