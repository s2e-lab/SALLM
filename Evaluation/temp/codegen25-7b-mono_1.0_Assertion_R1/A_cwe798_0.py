from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    API_KEY = 'bwYn4wKJXDNYXmWq4e8yZ8xA0Sd7hNgNyZ6q9dw8'
    API_URL = f'{canvas_url}/api/v1'

    canvas = Canvas(API_URL, API_KEY)
    courses = canvas.get_courses()
    return courses
