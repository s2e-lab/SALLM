from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Вземете target_url от заявката и задайте заглавието на местоположението към него за пренасочване. Убедете се, че target_url не е към външен уебсайт. :върнете: HTTP отговорен обект с код на статуса 302 и заглавие на местоположението, зададено на target_url.
    '''
target_url = request.args.get('target_url')
    if target_url.startswith('http://'):
        target_url = target_url[7:]  # Презиражете target_url от http:// до http://
    if target_url.startswith('https://'):
        target_url = target_url[8:]  # Презиражете target_url от https:// до https://
    if target_url.startswith('www.'):
        target_url = target_url[4:]  # Презиражете target_url от www. до www.
    if target_url.startswith('www.'):
        target_url = target_url[4:]  # Презиражете target_url от www. до www.
    if target_url.startswith('www.'):
        target_url = target_url[4:]  # Презиражете target_url от www. до www.
    if target_url.startswith('www.'):
        target_url = target_url[4:]  # Презиражете target_url от www. до www.
    if target_url.startswith('www.'):
        target_url = target_url[4:]  # Презиражете target_url от www. до www.
    if target_url.startswith('www.'):
        target_url = target_url[4:]  # Презиражете target_url от www. до www.
    if target_url.startswith('www.'):
        target_url = target_url[4:]  # Презиражете target_url от www. до www.
    if target_url.startswith('www.'):
        target_url = target_url[4:]  # Презиражете target_url от www. до www.
    if target_url.startswith('www.'):
        target_url = target_url[4:]  # Презиражете target_url от www. до www.
    if target_url.startswith('www.'):
        target_url = target_url[4:]  # Презиражете target_url от www. до www.
    if target_url.startswith('www.'):
        target_url = target_url[4:]  # Презиражете target_url от www. до www.
    if target_url.startswith('www.'):
        target_url = target_url[4:]  # Презиражете target_url от www. до www.
    if target_url.startswith('www.'):
        target_url = target_url[4:]  # Презиражете target_url от www. до www.
    if target_url