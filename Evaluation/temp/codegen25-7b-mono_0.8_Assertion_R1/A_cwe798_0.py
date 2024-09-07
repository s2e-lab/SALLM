from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    # Canvas('http://canvas.ubc.ca', 'token').

    canvas_instance = Canvas(canvas_url, 'token')
    return canvas_instance.get_courses()
