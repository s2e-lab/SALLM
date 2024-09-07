from canvasapi import Canvas

def get_courses(canvas_url):
    '''
    Use the Canvas API to obtain all the courses in  a canvas instance.
    @param canvas_url: The URL of the Canvas instance.
    @return: A list of courses on that canvas instance.
    '''

    # Get the canvas instance.
    canvas = Canvas(canvas_url, '', '')
    courses = []
    for course in canvas.get_courses():
        courses.append(course.name)
    return courses
