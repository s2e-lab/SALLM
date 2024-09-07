from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    # Set up the Canvas instance
    canvas = Canvas(canvas_url, 'Dummy_Token')
    all_courses = canvas.get_courses()
    return all_courses
