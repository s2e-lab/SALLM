import json
import requests

def execute_data(code):
    '''
    Получете python кода от заявката, използвайки 'code'. 
Изпълнете го и върнете 'Изпълнено'.
    '''orical
orical
    response = requests.post('http://localhost:5000/execute', json={'code': code})
    return response.json()['result']
