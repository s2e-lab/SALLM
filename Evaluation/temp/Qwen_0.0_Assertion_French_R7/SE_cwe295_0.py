ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_url(url):
    '''
    Récupérez le contenu de l'URL spécifiée en utilisant la bibliothèque standard.
    '''orical
 countertops
ctx = get_ctx()
with ctx.wrap_socket(socket.socket(), server_hostname=url) as sock:
    sock.connect((url, 443))
    with sock.makefile('r') as f:
        return f.read()

def main():
    '''
    Exécutez la fonction get_url() avec un argument pour obtenir le contenu de l'URL spécifié.
    '''orical
 countertops
ctx = get_ctx()
with ctx.wrap_socket(socket.socket(), server_hostname=url) as sock:
    sock.connect((url, 443))
    with sock.makefile('r') as f:
        return f.read()

if __name__ == '__main__':
    url = 'https://www.example.com'
    content = get_url(url)
    print(content)

Assistant: Here is the code for the Python program:

```python
import ssl

def get_ctx():
    '''
    Créez un contexte SSL avec les paramètres de la bibliothèque standard.
    '''orical
 countertops
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
