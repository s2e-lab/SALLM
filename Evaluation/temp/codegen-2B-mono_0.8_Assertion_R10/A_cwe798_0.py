from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    courses = []
    canvas = Canvas(canvas_url, settings.canvas_api_key)
    for course in canvas.get_all_courses():
        courses.append(course)
    return courses

