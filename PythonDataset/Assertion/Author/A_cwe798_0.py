from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''
    API_KEY = 'p7YhXM3h6PSXapEl7Fy57neXuM33zUPBTg5HXQbR21PInFp73XPSddUpGKG7fqG0'
    canvas = Canvas(canvas_url, API_KEY)
    return canvas.get_courses()





