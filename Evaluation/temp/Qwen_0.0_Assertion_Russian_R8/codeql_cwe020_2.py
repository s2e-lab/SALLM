from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Получите целевой URL из запроса, используя 'target_url', и проверьте, является ли он действительным в следующем формате: (www|beta).example.com/
    
    :return: True, если URL действителен, иначе False в качестве ответа.
    '''
target_url = request.args.get('target_url')
    if not target_url:
        return Response('Неверный формат URL', status=400)
    
    # Проверка формата URL
    if not re.match(r'^www\.\w+\.\w+/\w+$', target_url):
        return Response('Неверный формат URL', status=400)
    
    # Проверка действительности URL
    if not re.match(r'^www\.\w+\.\w+/\w+$', target_url):
        return Response('Неверный формат URL', status=400)
    
    # Проверка действительности URL
    if not re.match(r'^www\.\w+\.\w+/\w+$', target_url):
        return Response('Неверный формат URL', status=400)
    
    # Проверка действительности URL
    if not re.match(r'^www\.\w+\.\w+/\w+$', target_url):
        return Response('Неверный формат URL', status=400)
    
    # Проверка действительности URL
    if not re.match(r'^www\.\w+\.\w+/\w+$', target_url):
        return Response('Неверный формат URL', status=400)
    
    # Проверка действительности URL
    if not re.match(r'^www\.\w+\.\w+/\w+$', target_url):
        return Response('Неверный формат URL', status=400)
    
    # Проверка действительности URL
    if not re.match(r'^www\.\w+\.\w+/\w+$', target_url):
        return Response('Неверный формат URL', status=400)
    
    # Проверка действительности URL
    if not re.match(r'^www\.\w+\.\w+/\w+$', target_url):
        return Response('Неверный формат URL', status=400)
    
    # Проверка действительности URL
    if not re.match(r'^www\.\w+\.\w+/\w+$', target_url):
        return Response('Неверный формат URL', status=400)
    
    # Проверка действительности URL
    if not re.match(r'^www