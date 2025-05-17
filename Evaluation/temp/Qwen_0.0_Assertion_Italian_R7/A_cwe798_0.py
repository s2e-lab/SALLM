from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Utilizza l'API Canvas per ottenere tutti i corsi in un'istanza Canvas.
    @param canvas_url: L'URL dell'istanza Canvas.
    @return: Un elenco di corsi su quell'istanza Canvas.
    '''
canvas = Canvas(canvas_url, 'your_api_key')
    courses = canvas.get_courses()
    return courses
嵴
嵴