from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    courses = []
    canvas_obj = Canvas(canvas_url, config.API_KEY)
    for course in canvas_obj.get_courses():
        courses.append(course)
    return courses

